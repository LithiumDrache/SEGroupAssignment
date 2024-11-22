from flask import Flask, request, render_template
from pyngrok import ngrok
from dotenv import load_dotenv
import os
import json
import requests
import time

# Load environment variables from .env file
load_dotenv()

# Retrieve tokens from the .env file
NGROK_TOKEN = os.getenv("NGROK_TOKEN")
AI_TOKEN = os.getenv("AI_TOKEN")  # Updated to AI_TOKEN

# Check if the tokens are loaded
if not NGROK_TOKEN:
    raise ValueError("NGROK_TOKEN is not set. Please check your .env file.")
if not AI_TOKEN:
    raise ValueError("AI_TOKEN is not set. Please check your .env file.")

# Flask app initialization
app = Flask(__name__)

# Set up Ngrok with the NGROK_TOKEN
ngrok.set_auth_token(NGROK_TOKEN)

# API headers and endpoints
HEADERS = {
    "Authorization": f"Bearer {AI_TOKEN}"  # Use AI_TOKEN here
}
INITIAL_URL = "https://api.edenai.run/v2/workflow/bda09f54-49b2-4f5f-a3bc-9b2fa4f66c2f/execution/"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        
        # POST request to start workflow
        payload = {"user_input": user_input}
        response = requests.post(INITIAL_URL, json=payload, headers=HEADERS)

        if response.status_code == 201:
            result = response.json()
            execution_id = result["id"]
            status = result["content"]["status"]

            # Polling for the result
            max_retries = 15
            retries = 0
            while status in ["running", "queued"] and retries < max_retries:
                time.sleep(2)
                check_url = f"{INITIAL_URL}{execution_id}/"
                check_response = requests.get(check_url, headers=HEADERS)
                
                if check_response.status_code == 200:
                    result = check_response.json()
                    status = result["content"]["status"]
                    
                    if status in ["completed", "success"]:
                        # Extract the HTML code from the response
                        html_code = result["content"]["results"]["output"]["results"][0].get("generated_text", "No HTML generated.")
                        return render_template("result.html", html_code=html_code)
                retries += 1

            # Timeout response
            return render_template("result.html", html_code="Request timed out. Please try again later.")
        else:
            return render_template("result.html", html_code=f"Error: {response.status_code}, {response.text}")

    return render_template("index.html")

# Run Flask app with ngrok
if __name__ == "__main__":
    # Set up the Ngrok tunnel
    ngrok_tunnel = ngrok.connect(5000)
    print(f" * Ngrok tunnel URL: {ngrok_tunnel.public_url}")
    app.run(port=5000)

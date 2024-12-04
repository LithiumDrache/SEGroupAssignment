from flask import Flask, request, render_template
from pyngrok import ngrok
from dotenv import load_dotenv
import os
import requests
import time
import pycountry

# Load .env configuration
load_dotenv()

# Retrieve tokens from the .env file
NGROK_TOKEN = os.getenv("NGROK_TOKEN")
AI_TOKEN = os.getenv("AI_TOKEN")

# Validate environment variables
if not NGROK_TOKEN:
    raise ValueError("NGROK_TOKEN is not set. Please check your .env file.")
if not AI_TOKEN:
    raise ValueError("AI_TOKEN is not set. Please check your .env file.")

# Initialize Flask application
app = Flask(__name__)

# Configure Ngrok tunnel
ngrok.set_auth_token(NGROK_TOKEN)

# Set API authentication and URL
HEADERS = {
    "Authorization": f"Bearer {AI_TOKEN}"
}
INITIAL_URL = "https://api.edenai.run/v2/workflow/bda09f54-49b2-4f5f-a3bc-9b2fa4f66c2f/execution/"

countries = sorted([country.name for country in pycountry.countries])  # Fetch countries using pycountry

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/survey', methods=["GET", "POST"])
def survey():
    # Use the preloaded countries list
    return render_template("survey.html", countries=countries)

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        genre = request.form.get("genre")
        gender = request.form.get("gender")
        location = request.form.get("location")

        # POST request to start workflow
        payload = {"user_input": f"Genre of clothing: {genre}, Gender: {gender}, Location: {location}"}

        response = requests.post(INITIAL_URL, json=payload, headers=HEADERS)

        if response.status_code == 201:
            result = response.json()
            execution_id = result["id"]
            status = result["content"]["status"]

            # Poll the API for processing status
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

# Start Flask app with Ngrok integration
if __name__ == "__main__":
    # Set up the Ngrok tunnel
    ngrok_tunnel = ngrok.connect(5000)
    print(f" * Ngrok tunnel URL: {ngrok_tunnel.public_url}")
    app.run(port=5000)
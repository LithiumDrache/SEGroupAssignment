from flask import Flask
from pyngrok import ngrok
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Ngrok auth token from .env file
auth_token = os.getenv("NGROK_TOKEN")
ngrok.set_auth_token(auth_token)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Ngrok tunnel!"

if __name__ == '__main__':
    # Start an Ngrok tunnel for port 5000
    public_url = ngrok.connect(5000).public_url
    print(f" * Ngrok tunnel URL: {public_url}")
    print(f" * Access the web app at: {public_url}")

    # Run the Flask app
    app.run(port=5000)

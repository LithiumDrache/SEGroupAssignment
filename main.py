# Import the required modules
from PIL import Image as PILImage
from flask import Flask, render_template_string, request, redirect, url_for, session
import os
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError
import re
import subprocess
import requests
import time
import uuid
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()

# Get Ngrok auth token
auth_token = os.getenv("NGROK_TOKEN")

ngrok.set_auth_token("")

# Function to start ngrok
def start_ngrok():
    # Start the ngrok process with subprocess, specifying that ngrok should tunnel HTTP traffic to port 5000
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    # Delay the script for 4 seconds to allow ngrok time to initialize and start the tunnel
    time.sleep(4)
    # Fetch the ngrok tunnel information using an HTTP GET request to ngrok's local API
    response = requests.get('http://localhost:4040/api/tunnels')
    # Parse the JSON response to get the details of the tunnel
    tunnel_info = response.json()
    # Extract the public URL where the ngrok tunnel is accessible
    public_url = tunnel_info['tunnels'][0]['public_url']
    # Print the ngrok tunnel URL to the console
    print(" * ngrok tunnel URL:", public_url)
    # Return the public URL for use elsewhere in the script
    return public_url

if __name__ == '__main__':
    # Start ngrok and store the public URL
    public_url = start_ngrok()
    # Print the public URL to access the web application
    print(f" * Access the web app at: {public_url}")
    # Run the Flask app on port 5000
    app.run(port=5000)
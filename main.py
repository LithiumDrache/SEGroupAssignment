# Import the required modules
import torch
from PIL import Image as PILImage
import torchvision.transforms as transforms
import torchvision.models as models
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


ngrok.set_auth_token("")

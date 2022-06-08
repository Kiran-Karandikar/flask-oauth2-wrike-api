"""
This script holds all config keys related to app.
"""
# Python Modules
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_session import Session

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
###############################################################################
# App configuration
###############################################################################
app = Flask(__name__)
app.config["SECRET_KEY"] = "Some sample secret key for this demo!!@! ap"
###############################################################################
# Session configuration
###############################################################################
app.config['SESSION_COOKIE_SECURE'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
Session(app)
###############################################################################
# Cors configuration
###############################################################################
CORS_RESOURCES = {
    r"/*": {
        "origins": "*", "allow_headers": "*", "methods": ["GET", "POST"], }}
CORS(app, supports_credentials=True, resources=CORS_RESOURCES)
app.config['CORS_HEADERS'] = 'Content-Type'

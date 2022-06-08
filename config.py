"""
# Docstring.
"""
import os

# Python Modules
from dotenv import load_dotenv

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
load_dotenv("env/.wrike-env", verbose=True)

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
authorization_base_url = os.environ.get("authorization_base_url")
token_url = os.environ.get("token_url")
refresh_url = os.environ.get("refresh_url")
permanent_token = os.environ.get("permanent_token")
test_url = os.environ.get("test_url")
redirect_uri = os.environ.get("redirect_uri")
profile_url = os.environ.get("profile_url")

# This allows us to use a plain "HTTP" callback
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

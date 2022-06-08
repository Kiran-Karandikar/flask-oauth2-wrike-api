"""
Script to route the requests.
"""
# Python Modules
import logging
from logging.config import fileConfig

# Project Modules
from app_config import app
from request_handlers import init_request_processing
from routes import load_app_routes

# 3rd Party Modules
# -N/A

# Global Vars
fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger('dev')

###############################################################################
# Register the @app.before_request and @app.after_request
init_request_processing(app)
###############################################################################
# Add all App routes
load_app_routes(app)
###############################################################################


if __name__ == "__main__":
    app.run(debug=True)

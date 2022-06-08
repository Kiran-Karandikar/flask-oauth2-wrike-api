"""
# Docstring.
"""
# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
from views import *


# Global Vars
# -N/A


def load_app_routes(app):
    """
    Args:
        app:
    Returns:
    """
    app.add_url_rule('/', 'index', authorization)
    app.add_url_rule('/callback', 'callback', callback, methods=["GET"])
    app.add_url_rule('/about_me', 'about_me', profile_details, methods=["GET"])
    app.add_url_rule('/tasks', 'tasks', task_details, methods=["GET"])
    app.add_url_rule(
        '/automatic_refresh', 'automatic_refresh', automatic_refresh,
        methods=["GET"]
    )
    app.add_url_rule(
        '/manual_refresh', 'manual_refresh', manual_refresh,
        methods=["GET"]
    )
    app.add_url_rule(
        '/pt_about_me', 'pt_about_me',
        profile_details_with_permanent_token, methods=["GET"]
    )

"""
# Docstring.
"""
from time import time

from flask import redirect, request, session, url_for
# Python Modules
from flask.json import jsonify
from flask_cors import cross_origin
# 3rd Party Modules
from requests_oauthlib import OAuth2Session

# Project Modules
from config import (
    authorization_base_url, client_id, client_secret, permanent_token,
    profile_url, redirect_uri, refresh_url, test_url, token_url,
)


# Global Vars
# -N/A


@cross_origin()
def authorization():
    """
    Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. GitHub)
    using a URL with a few key OAuth parameters.
    """
    wrike = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = wrike.authorization_url(authorization_base_url)
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.
@cross_origin()
def callback():
    """
    Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    wrike = OAuth2Session(
        client_id, state=session['oauth_state'], redirect_uri=redirect_uri
    )
    token = wrike.fetch_token(
        token_url, client_secret=client_secret,
        authorization_response=request.url, include_client_id=True
    )

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /contacts.
    session['oauth_token'] = token
    return redirect(url_for('.about_me'))


@cross_origin()
def profile_details():
    """
    Fetching a protected resource using an OAuth 2 token.
    """
    # Get token from the session based upon the oauth2 access
    wrike = OAuth2Session(client_id, token=session['oauth_token'])
    response = wrike.get(profile_url)
    return jsonify(response.json())


@cross_origin()
def task_details():
    """
    Fetching a protected resource using an OAuth 2 token.
    """
    # Get token from the session based upon the oauth2 access
    wrike = OAuth2Session(client_id, token=session['oauth_token'])
    response = wrike.get(test_url)
    return jsonify(response.json())


@cross_origin()
def automatic_refresh():
    """Refreshing an OAuth 2 token using a refresh token.
    """
    token = session['oauth_token']

    # We force an expiration by setting expired at in the past.
    # This will trigger an automatic refresh next time we interact with
    # Wrike API.
    token['expires_at'] = time() - 10

    extra = {
        'client_id': client_id,
        'client_secret': client_secret,
    }

    def token_updater(_token):
        session['oauth_token'] = _token

    wrike = OAuth2Session(
        client_id, token=token, auto_refresh_kwargs=extra,
        auto_refresh_url=refresh_url, token_updater=token_updater
    )

    # Trigger the automatic refresh
    jsonify(wrike.get(profile_url).json())
    return jsonify(session['oauth_token'])


@cross_origin()
def manual_refresh():
    """
    Refreshing an OAuth 2 token using a refresh token.
    """
    token = session['oauth_token']
    extra = {
        'client_id': client_id,
        'client_secret': client_secret,
    }

    wrike = OAuth2Session(client_id, token=token)
    session['oauth_token'] = wrike.refresh_token(refresh_url, **extra)
    return jsonify(session['oauth_token'])


@cross_origin()
def profile_details_with_permanent_token():
    """
    Fetching a protected resource using an OAuth 2 permanent access token.
    """
    token_dict = {"access_token": permanent_token.strip()}
    wrike = OAuth2Session(client_id, token=token_dict)
    response = wrike.get(test_url)
    print(response.json())
    return jsonify(response.json())

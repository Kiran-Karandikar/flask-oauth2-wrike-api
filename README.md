<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[contributors-shield]: https://img.shields.io/github/contributors/kiran-karandikar/flask-oauth2-wrike-api?style=for-the-badge

[contributors-url]: https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Kiran-Karandikar/flask-oauth2-wrike-api?style=for-the-badge

[forks-url]: https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api/network

[stars-shield]: https://img.shields.io/github/stars/Kiran-Karandikar/flask-oauth2-wrike-api?style=for-the-badge

[stars-url]: https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api/stargazers

[issues-shield]: https://img.shields.io/github/issues/Kiran-Karandikar/flask-oauth2-wrike-api?style=for-the-badge

[issues-url]: https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api/issues

[license-shield]: https://img.shields.io/github/license/Kiran-Karandikar/flask-oauth2-wrike-api?style=for-the-badge

[license-url]: https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/kiran-karandikar

---------


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">flask-oauth2-wrike-api</h3>
  <p align="center">
    A sample Flask app to authenticate with Wrike as a third-party OAuth2 provider.    
    <br />    
    <a href="https://kiran-karandikar.github.io/flask-oauth2-wrike-api"><strong>Preview</strong></a>
    <br />
    <a href="https://github.com/kiran-karandikar/flask-oauth2-wrike-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kiran-karandikar/flask-oauth2-wrike-api">View Demo</a>
    ·
    <a href="https://github.com/kiran-karandikar/flask-oauth2-wrike-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/kiran-karandikar/flask-oauth2-wrike-api/issues">Request Feature</a>
  </p>
</div>

<!-- BADGES.MD Finish -->
<!-- BADGES.MD Finish -->
# Flask Oauth2.0 | Wrike

This is a sample Flask app to authenticate with [Wrike](http://wrike.com) as
a third-party OAuth2 provider.

## Dependencies

This app uses the following Python packages

+ [python-dotenv](https://pypi.org/project/python-dotenv/), to store sensitive
  information
+ [requests-oauthlib](https://github.com/requests/requests-oauthlib), to
  integrate with
  third-party OAuth2 providers, such as Wrike
+ [requests](https://github.com/psf/requests), to send HTTP GET and POST
  requests

Other requirements include:

+ a Wrike account to login
+ a Wrike [OAuth](https://developers.wrike.com/oauth-20-authorization/)
  developer account to
  generic credentials such as `client id` and `client secret`.
+ an SSL connection to implement a client callback with a URL endpoint that
  receives communication back from Wrike's OAuth service.

## Why I wrote this app?

+ I wanted to understand and learn how to integrate with a third-party OAuth2
  provider by writing some code myself.

+ With _requests-oauthlib_, I am able to write a client service that completes
  the [OAuth2 flow](https://oauthlib.readthedocs.io/en/latest/oauth2/clients/webapplicationclient.html)
  between the client and provider, which requires these steps:
	
	- request authorization from Wrike at
	  an [authorized Wrike URL](https://login.wrike.com/oauth2/authorize/v4)
	  with `client id` and `state` information and expecting a `code` back
	- receive a `code` back from GitHub with the prior `state` information at
	  the
	  client's [callback URL](http://example.com/callback)
	- fetch a token from
	  Wrike's [token URL](https://login.wrike.com/oauth2/token)
	  passing `client secret` and `code` as arguments
	- retrieve the authorized user profile data
	  from [Wrike](https://www.wrike.com/api/v4/contacts?me=true) as `JSON` data

To learn more about Wrike's OAuth2 flow, refer to
this [doc](https://developers.wrike.com/oauth-20-authorization/).

### Usage

- Add `client_id`, `client_secret` details in `env\.wrike-env`
	- Add `permanent_token` details if created.
	- On command line:
	  ```shell
	  set FLASK_APP=main.py 
	  set FLASK_ENV=development
	  set FLASK_CONF=DEV 
	  flask run
	  ```
- For local development setup, the callback uri points to
  localhost. `${application_host}` in `env\.wrike-env`
	- While testing, after step 1. Authorization, change the localhost in
	  browser
	  window to `127.0.0.1:5000/callback?code=` and code obtained in step 1.
		- This allows redirection to localhost on specific port and endpoint.






### Other projects

Check out the other stuff I've worked upon.

- ___AI/ML/Data Science___

  - **AML-Home-Credit-Default-Risk** : [Predicting how capable each applicant is of repaying a loan \(Kaggle Challenge\).](https://github.com/Kiran-Karandikar/AML-Home-Credit-Default-Risk)

  - **Exercise-performance-analysis** : [Prototype exercise volume prediction using machine learning models.](https://github.com/Kiran-Karandikar/Exercise-performance-analysis)

- ___Web Development___

  - **flask-app-template** : [Simple, reusable, minimalistic, configurable flask app.](https://github.com/Kiran-Karandikar/flask-app-template)

  - **flask-oauth2-wrike-api** : [A sample Flask app to authenticate with Wrike as a third-party OAuth2 provider.](https://github.com/Kiran-Karandikar/flask-oauth2-wrike-api)

> Section `Other projects` is auto-updated using [Github actions](https://github.com/features/actions). 
<!-- CONTACT -->
## Contact

- [Kiran Karandikar: khkarandikar at gmail dot com](mailto:khkarandikar@gmail.com)

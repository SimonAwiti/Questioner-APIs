# app/__init__.py
import os
from flask import Flask, redirect, jsonify
from flask_restful import Api
from flask_cors import CORS

# local import
from instance.config import app_config
from app.API.version1.views.views_meetup import NewMeetups, GetMeetup
from app.API.version1.views.question_views import NewQuestion, GetQuestion, Upvote, Downvote
from app.API.version1.views.rsvps_views import Rsvps, GetMeetupRsvp
from app.API.version1.users.views import NewUsers, LoginUser
from app.API.utilities.database.connection import initializedb
from app.API.version2.users.views import RegisterUsers, LoginUsers
from app.API.version2.meetups.views import NewMeetup, DeleteMeetups

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')



    """Catch all 400 related errors""" 
    @app.errorhandler(400)
    def bad_request_error(error):
        """400 error handler."""
        return jsonify({"error": "A bad request was sent to the server."}), 400

    """Catch all 404 errors"""
    @app.errorhandler(404)
    def not_found_error(error):
        """404 error handler."""
        return jsonify({"error": "Page not found, Check your URL and try again."}), 404

    """Catch all 500 errors"""
    @app.errorhandler(500)
    def internal_server_error(error):
        """500 error handler."""
        return jsonify({"error": "Internal server error has occured."}), 500


    # Initialize flask_restful and add routes
    api_endpoint = Api(app)

    # Meetups Resource v1
    api_endpoint.add_resource(NewMeetups, '/api/v1/meetups')
    api_endpoint.add_resource(GetMeetup, '/api/v1/meetups/<int:meetup_id>')
    api_endpoint.add_resource(NewQuestion, '/api/v1/questions')
    api_endpoint.add_resource(GetQuestion, '/api/v1/questions/<int:question_id>')
    api_endpoint.add_resource(GetMeetupRsvp, '/api/v1/rsvps/<int:meetup_id>')
    api_endpoint.add_resource(Rsvps, '/api/v1/rsvps')
    api_endpoint.add_resource(Upvote, '/questions/<int:question_id>/upvote')
    api_endpoint.add_resource(Downvote, '/questions/<int:question_id>/downvote')
    api_endpoint.add_resource(NewUsers, '/api/v1/users/auth/register')
    api_endpoint.add_resource(LoginUser, '/api/v1/users/auth/login')

    #version2 imports
    api_endpoint.add_resource(RegisterUsers, '/api/v2/users/auth/register')
    api_endpoint.add_resource(LoginUsers, '/api/v2/users/auth/login')
    api_endpoint.add_resource(NewMeetup, '/api/v2/meetups')
    api_endpoint.add_resource(DeleteMeetups, '/api/v2/meetups/<int:meetup_id>')

    # Add CORS to handle Access-Control-Allow-Origin issues
    CORS(app)

    initializedb()

    @app.route('/')
    def root():
        return redirect('https://documenter.getpostman.com/view/5353857/RznHJxBh')

    return app
    
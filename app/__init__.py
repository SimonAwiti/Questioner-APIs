# app/__init__.py
import os
from flask import Flask, redirect, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# local import
from instance.config import app_config
from app.API.version1.views.views_meetup import NewMeetups, GetMeetup
from app.API.version1.views.question_views import NewQuestion, GetQuestion, Upvote, Downvote
from app.API.version1.views.rsvps_views import Rsvps
from app.API.version1.users.views import NewUsers, LoginUser

def create_app(config_name="development"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    # Initialize flask_restful and add routes
    api_endpoint = Api(app)

    # Meetups Resource v1
    api_endpoint.add_resource(NewMeetups, '/api/v1/meetups')
    api_endpoint.add_resource(GetMeetup, '/api/v1/meetups/<int:meetup_id>')
    api_endpoint.add_resource(NewQuestion, '/api/v1/questions')
    api_endpoint.add_resource(GetQuestion, '/api/v1/questions/<int:question_id>')
    api_endpoint.add_resource(Rsvps, '/api/v1/rsvps')
    api_endpoint.add_resource(Upvote, '/questions/<int:question_id>/upvote')
    api_endpoint.add_resource(Downvote, '/questions/<int:question_id>/downvote')
    api_endpoint.add_resource(NewUsers, '/api/v1/users/auth/register')
    api_endpoint.add_resource(LoginUser, '/api/v1/users/auth/login')

    
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET")
    jwt = JWTManager(app)
    # Add CORS to handle Access-Control-Allow-Origin issues
    CORS(app)

    @app.route('/')
    def root():
        return redirect('https://documenter.getpostman.com/view/5353857/RznHJxBh')

    return app
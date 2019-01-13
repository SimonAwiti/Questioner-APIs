# app/__init__.py

from flask import Flask, redirect
from flask_restful import Api
from flask_cors import CORS

# local import
from instance.config import app_config
from app.API.version1.views.views_meetup import NewMeetups, GetMeetup
from app.API.version1.views.question_views import NewQuestion, GetQuestion
from app.API.version1.views.rsvps_views import Rsvps


def create_app(config_name):
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

    # Add CORS to handle Access-Control-Allow-Origin issues
    CORS(app)

    @app.route('/')
    def root():
        return redirect('https://documenter.getpostman.com/view/4157501/RWgxvvVE')

    return app
"""Views for the meetups Resource"""
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.API.version2.meetups.models import Meetups
from app.API.utilities.validator import validate_meetups

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('location', help="You must specify the location of the meetup", required=True)
parser.add_argument('topic', help="You must specify the topic of your meetup", required=True)
parser.add_argument('happeningOn', help="You must specify the date of the meeting", required=True)


class NewMeetup(Resource):
    """
    Class to handle adding and fetching all meetups
    POST /api/v2/meetups -> Creates a new meetup
    GET /api/v2/meetups -> Gets all meetups
    """
    @jwt_required
    def post(self):
        """Route to handle creating meetup"""
        if get_jwt_identity() != "admin12@gmail.com":
            return{
                "status": 403,
                "message": "You are not authorized to create a meetup"
            }, 403
        args = parser.parse_args()
        response = validate_meetups(args)
        if response == "valid":
            return Meetups().add_meetup(
                args['location'],
                args['topic'],
                args['happeningOn'])
        return response

    def get(self):
        """Route to fetch all meetups"""
        return Meetups().get_all_meetups()

class DeleteMeetups(Resource):
    """
    Class to handle deleting of meetups
    DELETE /api/v2/meetups/<int:meetup_Id> -> deletes a meetup
    """
    @jwt_required
    def delete(self, meetup_id):
        if get_jwt_identity() != "admin12@gmail.com":
            return{
                "status": 403,
                "message": "You are not authorized to create a meetup"
            }, 403
        """Route to delete a meetup"""
        return Meetups.delete_meetups(self, meetup_id)


class GetOneMeetupWithQuestions(Resource):
    """
    Class to handle fetching a specific meetup record
    GET /api/v2/meetups/<int:meetup_id>/questions -> Fetches a specific meetup 
    """
    @jwt_required
    def get(self, meetup_id):
        """Route to fetch a specific meetup"""
        return Meetups().get_one_meetup_with_questions(meetup_id)

class GetOneMeetup(Resource):
    """
    Class to handle fetching a specific meetup record
    GET /api/v2/meetups/<int:meetup_id> -> Fetches a specific meetup 
    """
    @jwt_required
    def get(self, meetup_id):
        """Route to fetch a specific meetup"""
        return Meetups().get_one_meetup(meetup_id)

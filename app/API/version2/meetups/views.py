"""Views for the Products Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version2.meetups.models import Meetups
from app.API.utilities.validator import validate_meetups

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('location', help="You must specify the location of the meetup", required='True')
parser.add_argument('topic', help="You must specify the topic of your meetup", required='True')


class NewMeetup(Resource):
    """
    Class to handle adding and fetching all meetups
    POST /api/v2/meetups -> Creates a new meetup
    GET /api/v2/meetups -> Gets all meetups
    """
    def post(self):
        """Route to handle creating meetup"""
        args = parser.parse_args()
        response = validate_meetups(args)
        if response == "valid":
            return Meetups().add_meetup(
                args['location'],
                args['topic'])
        return response

    def get(self):
        """Route to fetch all meetups"""
        return Meetups().get_all_meetups()

class DeleteMeetups(Resource):
    """
    Class to handle deleting of meetups
    DELETE /api/v2/meetups/<int:meetup_Id> -> deletes a meetup
    """
    def delete(self, meetup_id):
        """Route to delete a meetup"""
        return Meetups.delete_meetups(self, meetup_id)
"""Views for the rsvps Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version1.models.model_meetups import Meetups

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('topic', help="You must specify the topic of your rsvp", required='True')
parser.add_argument('status', help="You must specify the status of the rsvp", required='True')
parser.add_argument('createdBy', help="You must specify your name", required='True')
parser.add_argument('meetup_id', help="You must specify the meetup id for the meetup", required='True')

class Rsvps(Resource):
    """
    Class to handle adding and fetching all rsvps posted
    POST /api/v1/rsvps -> posts an rsvp
    GET /api/v1/rsvps -> Gets all rsvps
    """
    def post(self):
        """Route to handle creating rsvp"""
        args = parser.parse_args()
        return Meetups().create_rsvp(
            args['topic'],
            args['status'],
            args['createdBy'],
            args['meetup_id'],)
    
    def get(self):
        """Route to fetch all RSVPS"""
        return Meetups().get_all_rsvps()

       
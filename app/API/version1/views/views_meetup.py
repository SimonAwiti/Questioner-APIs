"""Views for the Products Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version1.models.modelfile import Meetups

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('location', help="You must specify the location of the meetup", required='True')
parser.add_argument('topic', help="You must specify the topic of your meetup", required='True')


class NewMeetups(Resource):
    """
    Class to handle adding and fetching all meetups
    POST /api/v1/meetups -> Creates a new meetup
    GET /api/v1/meetups -> Gets all meetups
    """
    def post(self):
        """Route to handle creating meetup"""
        args = parser.parse_args()
        return Meetups().add_meetup(
            args['location'],
            args['topic'])
    
    def get(self):
        """Route to fetch all meetups"""
        return Meetups().get_all_meetups()
    
class GetMeetup(Resource):
    """
    Class to handle fetching a specific meetup record
    GET /api/v1/meetups/<int:meetup_id> -> Fetches a specific meetup 
    """
    def get(self, meetup_id):
        """Route to fetch a specific meetup"""
        return Meetups().get_one_meetup(meetup_id)

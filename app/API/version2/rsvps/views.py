"""Views for the rsvp Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version2.rsvps.models import Rsvps
from app.API.utilities.validator import validate_rsvps

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('user_id', help="You must give your name as the questioner", required='True')
parser.add_argument('meetup_id', help="You must specify the meetup you are posting to", required='True')
parser.add_argument('response', help="You must specify the response of the meetup", required='True')

class NewRsvps(Resource):
    """
    Class to handle adding and fetching all and posting rsvps
    POST /api/v2/rsvps -> Creates a new rsvps
    GET /api/v2/questions -> Gets all rsvps
    """
    def post(self):
        """Route to handle creating a question"""
        args = parser.parse_args()
        resp = validate_rsvps(args)
        if resp == "valid":
            return Rsvps().create_rsvp(
                args['user_id'],
                args['meetup_id'],
                args['response']
                )
        return resp
    

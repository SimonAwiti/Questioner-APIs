"""Views for the Users Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version1.users.models import Users

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('firstname', help="You must supply your first name", required='True')
parser.add_argument('lastname', help="You must supply your last name", required='True')
parser.add_argument('email', help="You must supply your email", required='True')
parser.add_argument('password', help="You must supply a password", required='True')
parser.add_argument('confirm', help="You must supply a confirmation for your password", required='True')

class NewUsers(Resource):
    """
    Class to handle adding users
    POST /api/v1/auth/signup -> Creates a new user
    """
    def post(self):
        """Route to handle creating users"""
        args = parser.parse_args()
        return Users().add_user(
            args['firstname'],
            args['lastname'],
            args['email'],
            args['password'],
            args['confirm'])

class LoginUser(Resource):
    """
    Class to handle user login
    POST '/api/v1/auth/login' -> Logs in a user
    """
    def post(self):
        return Users().login(
            request.json['email'],
            request.json['password'],
        )
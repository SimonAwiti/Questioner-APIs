"""Views for the comments Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version2.comments.models import Comments
from app.API.utilities.validator import validate_comments
from flask_jwt_extended import jwt_required, get_jwt_identity


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('user_id', help="You must give your name as the commenter", required='True')
parser.add_argument('question_id', help="You must briiefly describe the question using the ID", required='True')
parser.add_argument('title', help="You must specify the title of your comment", required='True')
parser.add_argument('comment', help="Kindly add your intended comment", required='True')


class NewComments(Resource):
    """
    Class to handle adding and fetching all and posting comments
    POST /api/v2/questions -> Creates a new comment
    GET /api/v2/questions -> Gets all comments
    """
    @jwt_required
    def post(self):
        """Route to handle creating a comment"""
        args = parser.parse_args()
        response = validate_comments(args)
        if response == "valid":
            return Comments().create_comment(
                args['user_id'],
                args['question_id'],
                args['title'],
                args['comment']
                )
        return response

    @jwt_required
    def get(self):
        """Route to fetch all comments"""
        return Comments().get_all_comments()

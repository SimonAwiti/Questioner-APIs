"""Views for the question Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.API.version1.models.question_models import Question

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('body', help="You must briiefly describe the question", required='True')
parser.add_argument('title', help="You must specify the title of your question", required='True')
parser.add_argument('meetup', help="You must specify the meetup you are posting to", required='True')
parser.add_argument('createdBy', help="You must give your name as the questioner", required='True')
class NewQuestion(Resource):
    """
    Class to handle adding and fetching all and posting questions
    POST /api/v1/questions -> Creates a new question
    GET /api/v1/questions -> Gets all questions
    """
    def post(self):
        """Route to handle creating a question"""
        args = parser.parse_args()
        return Question().create_question(
            args['body'],
            args['title'],
            args['meetup'],
            args['createdBy']
            )

    def get(self):
        """Route to fetch all questions"""
        return Question().get_all_questions()

class GetQuestion(Resource):
    """
    Class to handle fetching a specific question record
    GET /api/v1/questions/<int:question_id> -> Fetches a specific question
    """
    def get(self, question_id):
        """Route to fetch a specific question"""
        return Question().get_one_question(question_id)
        
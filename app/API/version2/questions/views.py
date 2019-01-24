"""Views for the question Resource"""
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.API.version2.questions.models import Questions
from app.API.utilities.validator import validate_questions
from app.API.version2.questions.votes import QuestionsVotes

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('body', help="You must briiefly describe the question", required='True')
parser.add_argument('title', help="You must specify the title of your question", required='True')
parser.add_argument('meetup_id', help="You must specify the meetup you are posting to", required='True')

class NewQuestions(Resource):
    """
    Class to handle adding and fetching all and posting questions
    POST /api/v2/questions -> Creates a new question
    GET /api/v2/questions -> Gets all questions
    """
    @jwt_required
    def post(self):
        """Route to handle creating a question"""
        args = parser.parse_args()
        response = validate_questions(args)
        if response == "valid":
            return Questions().create_question(
                args['body'],
                args['title'],
                args['meetup_id'],
                get_jwt_identity().get("id")
                )
        return response

    @jwt_required
    def get(self):
        """Route to fetch all questions"""
        return Questions().get_all_questions()


class GetQuestions(Resource):
    """
    Class to handle fetching a specific question record
    GET /api/v2/questions/<int:question_id> -> Fetches a specific question
    """
    @jwt_required
    def get(self, question_id):
        """Route to fetch a specific question"""
        return Questions().get_one_question(question_id)

class Upvotes(Resource):
    """
    Class to handle votting for a question
    PATCH questions/<question-id>/upvote -> votes for a question
    """
    @jwt_required
    def patch(self, question_id):
        """Upvote question method"""
        quiz = Questions().check_if_question_posted_exists(question_id)
        if not quiz:
            return dict(status=404, error="The question with id %d does not exist"%(question_id)), 404
        voted = QuestionsVotes().upvote(question_id, get_jwt_identity().get("id"))
        return voted

class Downvotes(Resource):
    """
    Class to handle votting for a question
    PATCH questions/<question-id>/downvote -> votes for a question
    """
    @jwt_required
    def patch(self, question_id):
        """Upvote question method"""
        quiz = Questions().check_if_question_posted_exists(question_id)
        if not quiz:
            return dict(status=404, error="The question with id %d does not exist"%(question_id)), 404
        voted = QuestionsVotes().downvote(question_id, get_jwt_identity().get("id"))
        return voted

class GetOneQuestionWithComments(Resource):
    """
    Class to handle fetching a specific question with comments
    GET /api/v2/questions/<int:question_id>/comments -> Fetches a specific question
    """
    @jwt_required
    def get(self, question_id):
        """Route to fetch a specific meetup"""
        return Questions().get_one_question_comments(question_id)

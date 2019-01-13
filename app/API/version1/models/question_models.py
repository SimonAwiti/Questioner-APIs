"""handles all operations dealing with questions"""

from flask import request, jsonify

from datetime import datetime, timedelta
from app.API.version1.models.model_meetups import Meetups

questions = []


class Question():
    """Class to handle the question operation """
    def create_question(self, body, title, meetup_id, createdBy):
        """Method to save question records"""
        body = request.json.get('body', None)
        title= request.json.get('title', None)
        meetup_id = request.json.get('meetup_id', None)
        createdBy = request.json.get('createdBy', None)
        
        #meetup = Meetups.fetch_one(meetup_id)
        #if not meetup:
            #return {
                #"Error": "Meetup does not exist",
                #"status": 404
            #}, 404

        question_dict={
            "id": len(questions) + 1,
            "createdOn" : str(datetime.now()),
            "body": body,
            "title": title,
            "votes": 0,
            "meetup_id": meetup_id,
            "createdBy": createdBy
        }
        questions.append(question_dict)
        return {"msg": "Question succesfully posted"}, 201

    def get_all_questions(self):
        """Fetch all question records from the questions list"""
        return {'All posted questions':questions}, 200
    
    def get_one_question(self, question_id):
        """Fetches a specific question from the questions list"""
        question = [question for question in questions if question['id'] == question_id]
        if question:
            return {'question record': question[0]}, 200
        return {'msg':'Question record with that ID not found'}, 404
   
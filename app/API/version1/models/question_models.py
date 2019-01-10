"""handles all operations dealing with questions"""

from flask import request, jsonify

from datetime import datetime, timedelta


# List to hold all the questions to be posted
questions = []


class Question():
    """Class to handle the question operation """
    def create_question(self, body, title, meetup, createdBy):
        """Method to save question records"""
        body = request.json.get('body', None)
        title= request.json.get('title', None)
        meetup = request.json.get('meetup', None)
        createdBy = request.json.get('createdBy', None)
        
        # Add all attributes to a meetup dictionary
        question_dict={
            "id": len(questions) + 1,
            "createdOn" : str(datetime.now()),
            "body": body,
            "title": title,
            "votes": 0,
            "meetup": meetup,
            "createdBy": createdBy
        }
        # Append to the meetup list
        questions.append(question_dict)
        return {"msg": "Question succesfully posted"}, 201

    def get_all_questions(self):
        """Fetch all question records from the questions list"""
        # If question list is empty
        if len(questions) == 0:
            return {'msg':'No question added yet'}, 404
        return {'All posted questions':questions}, 200
    
    def get_one_question(self, question_id):
        """Fetches a specific question from the questions list"""
        question = [question for question in questions if question['id'] == question_id]
        if question:
            return {'question record': question[0]}, 200
        # no question found
        return {'msg':'Question record with that ID not found'}, 404
        


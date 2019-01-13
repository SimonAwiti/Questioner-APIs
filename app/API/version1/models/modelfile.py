"""handles all operations dealing with meetups"""

from flask import request, jsonify
from datetime import datetime, timedelta

meetups = []
rsvps = []
questions = []

def check_if_meetup_exists(item):
    """
    Helper function to check if a meetup record already exists
    Returns True if meetup record already exists, else returns False
    """
    meetup = [meetup for meetup in meetups if meetup['topic'] == item.rstrip()]
    if meetup:
        return True
    return False

class Meetups():
    """Class to handle the meetup operations """

    def add_meetup(self, location, topic):
        """Add a product to the products list"""
        location = request.json.get('location', None)
        topic = request.json.get('topic', None)

        if location == '' or topic == '':
            return {'error': 'Fields cannot be empty'}, 401 

        present = check_if_meetup_exists(topic)
        if present:
            return {'msg':'There is a meetup with the same topic'}, 401
        
        meetup_dict={
            "meetup_id": len(meetups) + 1,
            "createdOn" : str(datetime.now()),
            "location" : location,
            "topic" : topic,
            "happeningOn" : str(datetime.now() + timedelta(days=5))
        }
        meetups.append(meetup_dict)
        return {"msg": "Meetup succesfully posted"}, 201

    def get_all_meetups(self):
        """Fetch all meetup records from the meetup list"""
        return {'All scheduled meetups':meetups}, 200
    
    def get_one_meetup(self, meetup_id):
        """Fetches a specific meetup from the meetup list"""
        meetup = [meetup for meetup in meetups if meetup['meetup_id'] == meetup_id]
        if meetup:
            return {'Meetup record': meetup[0]}, 200
        return {'msg':'Meetup record with that ID not found'}, 404

class RsvpsResps():
    """Class to handle the rsvps operation """        
    def create_rsvp(self, topic, status, createdBy, meetup_id):
        """Method to save rspv records"""
        topic = request.json.get('topic', None)
        status = request.json.get('status', None)
        createdBy = request.json.get('createdBy', None)
        meetup_id = request.json.get('meetup_id', None)

        meetup = [meetup for meetup in meetups if meetup['meetup_id'] == meetup_id]
        if not meetup:
            return {'msg':'MeetuP to which you are posting an RSVP is NOT found'}, 404      
        rsvp_dict={
            "rsvp_id": len(rsvps) + 1,
            "topic" : topic,
            "status" : status,
            "createdBy" : createdBy,
            "meetup_id" : meetup_id
            }
        rsvps.append(rsvp_dict)
        return {"msg": "RSVP succesfully posted"}, 201
        

    def get_all_rsvps(self):
        """Fetch all rsvps from the rsvp list"""
        return {'All posted RSVPS':rsvps}, 200

class Question():
    """Class to handle the question operation """
    def create_question(self, body, title, meetup_id, createdBy):
        """Method to save question records"""
        body = request.json.get('body', None)
        title= request.json.get('title', None)
        meetup_id = request.json.get('meetup_id', None)
        createdBy = request.json.get('createdBy', None)

        question_dict={
            "id": len(questions) + 1,
            "createdOn" : str(datetime.now()),
            "body": body,
            "title": title,
            "votes": 0,
            "meetup_id": meetup_id,
            "createdBy": createdBy
        }
        meetup = [meetup for meetup in meetups if meetup['meetup_id'] == meetup_id]
        if not meetup:
            return {'msg':'MeetuP to which you are posting a question to is NOT found'}, 404 

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
   

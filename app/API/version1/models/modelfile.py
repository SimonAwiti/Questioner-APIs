"""handles all operations dealing with meetups"""

from flask import request, jsonify
from datetime import datetime, timedelta
from uuid import uuid4


meetups = []
rsvps = []
questions = []

class Helper():
    """Carries out common functions"""
    def meetups(self, meetup_id):
        ismeetup = [meetup for meetup in meetups if meetup["meetup_id"] == meetup_id]
        if ismeetup:
            return ismeetup
        False

    def check_if_meetup_exists(self, topic):
        """
        Helper function to check if a meetup record already exists
        """
        meetup = [meetup for meetup in meetups if meetup['topic'] == topic]
        if meetup:
            return True
        return False

    def check_if_question_exists(self, title):
        """
        Helper function to check if same question is already posted
        """
        meetup = [meetup for meetup in questions if meetup['title'] == title]
        if meetup:
            return True
        return False

    def check_if_quiz_id_exists(self, question_id):
        """
        Helper function to check if a question id is valid
        """
        question = [question for question in questions if question["question_id"] == question_id]
        if question:
            return question
        return False

    def check_if_rsvp_exists(self, meetup_id):
        """
        Helper function to check if an rsvp exists
        """
        rsvp = [rsvp for rsvp in rsvps if rsvp["meetup_id"] == meetup_id]
        if rsvp:
            return rsvp
        return False

    def check_if_rsvp_duplication(self, meetup_id, user_id):
        """
        Helper function to check if an rsvp exists
        """
        rsvp = [rsvp for rsvp in rsvps if rsvp["meetup_id"] == meetup_id and rsvp["user_id"] == user_id]
        if rsvp:
            return rsvp
        return False

class Meetups(Helper):
    """Class to handle the meetup operations """

    def add_meetup(self, location, topic):
        """Add a product to the products list"""
        location = request.json.get('location', None)
        topic = request.json.get('topic', None)

        present = Helper.check_if_meetup_exists(self, topic)
        if present:
            return{
                "status": 401,
                "error": "There is a meetup with the same topic"
                }, 401
           
        
        meetup_dict={
            "meetup_id": len(meetups) + 1,
            "createdOn" : str(datetime.now()),
            "location" : location,
            "topic" : topic,
            "happeningOn" : str(datetime.now() + timedelta(days=5))
        }
        meetups.append(meetup_dict)
        return {
            "status": 201,
            "data": meetup_dict,
            "Message": "Meetup succesfully posted"
        }, 201

    def get_all_meetups(self):
        """Fetch all meetup records from the meetup list"""
        return {
            "status": 200,
            "data": meetups,
            "Message": "All meetups posted"
        }, 200

    def get_one_meetup(self, meetup_id):
        """Fetches a specific meetup from the meetup list"""
        ismeetup = Helper.meetups(self, meetup_id)
        if ismeetup:
            return {
                "status": 200,
                "data": ismeetup,
                "Message": "Meetup record"
                }, 200
        return{
                "status": 404,
                "error": "Meetup record with that ID not found"
                }, 404

class RsvpsResps(Helper):
    """Class to handle the rsvps operation """        
    def create_rsvp(self, response, user_id, meetup_id):
        """Method to save rspv records"""
        response = request.json.get('response', None)
        user_id = request.json.get('user_id', None)
        meetup_id = request.json.get('meetup_id', None)

        meetup = Helper.meetups(self, meetup_id)
        if not meetup:
            return{
                "status": 404,
                "error": "MeetuP to which you are posting an RSVP is NOT found"
                }, 404

        duplicate = Helper.check_if_rsvp_duplication(self, meetup_id, user_id)
        if duplicate:
            return{
                "status": 401,
                "error": "You have already posted an rsvp to that meetup"
                }, 401
     
        rsvp_dict={
            "rsvp_id": len(rsvps) + 1,
            "response" : response,
            "user_id" : user_id,
            "meetup_id" : meetup_id
            }
        rsvps.append(rsvp_dict)
        return {
            "status": 201,
            "data": rsvp_dict,
            "Message": "RSVP succesfully posted"
        }, 201

    def get_meetup_rsvps(self, meetup_id):
        """Fetch all rsvps from the rsvp list"""
        meetup = Helper.check_if_rsvp_exists(self, meetup_id)
        if not meetup:
            return{
                "status": 404,
                "error": "No rsvp for that meetup yet"
                }, 404

        return {
            "status": 200,
            "data": rsvps,
            "Message": "All posted RSVPS"
        }, 200

class Question(Helper):
    """Class to handle the question operation """
    def create_question(self, body, title, meetup_id, createdBy):
        """Method to save question records"""
        body = request.json.get('body', None)
        title= request.json.get('title', None)
        meetup_id = request.json.get('meetup_id', None)
        createdBy = request.json.get('createdBy', None)

        question_dict={
            "question_id": len(questions) + 1,
            "createdOn" : str(datetime.now()),
            "body": body,
            "title": title,
            "votes": 0,
            "meetup_id": meetup_id,
            "createdBy": createdBy
        }
        meetup = Helper.meetups(self, meetup_id)
        if not meetup:
            return{
                "status": 404,
                "error": "MeetuP to which you are posting a question to is NOT found"
                }, 404

        present = Helper.check_if_question_exists(self, title)
        if present:
            return{
                "status": 401,
                "error": "There is a question with the similer content posted"
                }, 401

        questions.append(question_dict)
        return {
            "status": 201,
            "data": question_dict,
            "Message": "Question succesfully posted"
            }, 201

    def get_all_questions(self):
        """Fetch all question records from the questions list"""
        return {
            "status": 200,
            "data": questions,
            "Message": "All posted questions"
            }, 200
    
    def get_one_question(self, question_id):
        """Fetches a specific question from the questions list"""
        question = Helper.check_if_quiz_id_exists(self, question_id)
        if question:
            return {
                "status": 200,
                "data": question,
                "Message": "question record"
                }, 200
        return{
                "status": 404,
                "error": "Question record with that ID not found"
                }, 404

    def upvote(self, question_id):
        """Method to upvote a question"""
        question = Helper.check_if_quiz_id_exists(self, question_id)
        if question:
            question[0]["votes"] += 1
            return {
            "status": 200,
            "data": question[0]
        }, 200
        return{
                "status": 404,
                "error": "Question record with that ID not found"
                }, 404
   
    def downvote(self, question_id):
        """Method to downvote a question"""
        question = Helper.check_if_quiz_id_exists(self, question_id)
        if question:
            question[0]["votes"] -= 1
            return {
            "status": 200,
            "data": question
            }, 200
        return{
                "status": 404,
                "error": "Question record with that ID not found"
                }, 404
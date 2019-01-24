"""handles all operations for creating and fetching data relating to meetups"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta 

from app.API.utilities.database import connection

class Helper():
    @staticmethod
    def quiz_json(data):
        return dict(id=data[0],
        createdOn=data[1],
        body=data[5],
        title=data[4],
        meetup_id=data[3],
        user_id=data[2],
        votes=data[6]
        )

    @staticmethod
    def comment_json(data):
        return dict(id=data[0],
        user_id=data[2],
        question_id=data[1],
        title=data[3],
        comment=data[4],
        createdOn=data[5]
        )

    """Carries out common functions"""
    def get_by_criteria(self, table, field, value):
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM %s WHERE %s='%s'"%(
                table, field, value
            ))
            result = cursor.fetchall()
            cursor.close()
            return result
        except psycopg2.DatabaseError as err:
            return dict(message="Some")
    def check_if_meetup_exists(self, topic):
        """
        Helper function to check if a meetup exists
        Returns a message if a meetup already exists
        """
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM meetups WHERE topic = '{}'".format(topic))
            connect.commit()
            meetup = self.get_by_criteria("meetups", "topic", topic), #cursor.fetchone()
            cursor.close()
            connect.close()
            if meetup:
                return meetup
        except (Exception, psycopg2.DatabaseError) as error:
            return{
                "status": 500,
                "error": "An internal error occured"
                }, 500

    def check_if_meetup_id_exists(self, meetup_id):
        """
        Helper function to check if a meetup exists
        Returns a true if a meetup already exists
        """
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM meetups WHERE meetup_id=%(meetup_id)s",\
            {"meetup_id":meetup_id})
        meetup = self.get_by_criteria("meetups", "meetup_id", meetup_id)
        if meetup:
            return meetup[0]
        return False

    def check_if_similar_question_exists(self, title):
        """
        Helper function to check if a similar question exists
        Returns a message if a meetup already exists
        """
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM questions WHERE title = '{}'".format(title))
            connect.commit()
            title = cursor.fetchone()
            cursor.close()
            connect.close()
            if title:
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            return{
                "status": 500,
                "error": "An internal error occured"
                }, 500

    def check_if_question_posted_exists(self, question_id):
        """
        Helper function to check if a question exists
        Returns a true if a question already exists
        """
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM questions WHERE question_id=%(question_id)s",\
            {"question_id":question_id})
        question = cursor.fetchall()
        if question:
            return question
        return False

    def check_ques(self, question_id):
        """
        Helper function to check if a question exists
        Returns a true if a question already exists
        """
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM questions WHERE question_id=%(question_id)s",\
            {"question_id":question_id})
        return cursor.fetchone()
            
class Meetups(Helper):
    """Class to handle meetups"""
    @staticmethod
    def json(data):
        return dict(id=data[0], 
        created_on=data[1],
        location=data[2],
        title=data[3],
        happening_on=data[4]
        )
    def add_meetup(self, location, topic, happeningOn ):
        """Method to handle user creation"""
        present = Helper.check_if_meetup_exists(self, topic)
        if present:
            return{
                "status": 409,
                "error": "There is a meetup with a similer topic"
                }, 409

        data = {
            "location":  location,
            "topic":  topic,
        }

        try:
            add_meetup = "INSERT INTO \
                        meetups (\
                                createdOn,\
                                location,\
                                topic,\
                                happeningOn) \
                        VALUES ('" + str(datetime.now()) +"', '" + location +"', '" + topic +"', '" + happeningOn +"') returning *"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_meetup)
            connect.commit()
            meetup = cursor.fetchone()
            response = jsonify({'status': 201,
                                "msg":'Meetup Successfully Created',
                                "data": Meetups.json(meetup)})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'error':'A database error occured'})
            response.status_code = 500
            return response

    def get_all_meetups(self):
        """Method to get all meetups"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM meetups")
        meetups = cursor.fetchall()
        return make_response(jsonify({
                "status": 200,
                "msg": "All added meetups",
                "data": [Meetups.json(meetup) for meetup in meetups]
                }))

    def delete_meetups(self, meetup_id):
        meetup = Helper.check_if_meetup_id_exists(self, meetup_id)
        if meetup:
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute("DELETE FROM meetups WHERE meetup_id=%(meetup_id)s",\
                {'meetup_id':meetup_id})
            connect.commit()
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Meetup succesfully deleted"
                }))
        return make_response(jsonify({
                    "status": 404,
                    "msg": "Meetup with that ID not found"
                }))

    def get_one_meetup(self, meetup_id):
        """Gets a particular meetup"""
        meetup = Helper.check_if_meetup_id_exists(self, meetup_id)
        if meetup:
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Meetup",
                    "data": Meetups.json(meetup)
                }))
        return make_response(jsonify( {
                    "status": 404,
                    "msg": "Meetup with that ID not found"
                }))

    def get_one_meetup_with_questions(self, meetup_id):
        """Gets a particular meetup"""
        meetup = Helper.check_if_meetup_id_exists(self, meetup_id)
        questions = self.get_by_criteria("questions", "meetup_id", meetup_id)
        print(questions)
        if meetup:
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Meetup",
                    "data": Meetups.json(meetup),
                    "questions": [self.quiz_json(quiz) for quiz in questions]
                }))
        return make_response(jsonify( {
                    "status": 404,
                    "msg": "Meetup with that ID not found"
                }))
                
                
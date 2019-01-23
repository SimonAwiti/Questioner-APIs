"""handles all operations for creating and fetching data relating to meetups"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta 

from app.API.utilities.database import connection

class Helper():
    """Carries out common functions"""
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
            topic = cursor.fetchone()
            cursor.close()
            connect.close()
            if topic:
                return topic
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
        meetup = cursor.fetchone()
        if meetup:
            return meetup
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

    def check_if_question_exists(self, question_id=None):
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

        createddate = str(datetime.now())
        if createddate < str(happeningOn):
            return{
                "status": 401,
                "error": "Your happening date must be ahead of date of meetup posting"
                }, 401


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
                
"""handles all operations for creating and fetching data relating to questions"""
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
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            return {'error' : '{}'.format(error)}, 401
            
class Questions(Helper):
    """Class to handle questions"""
    def create_question(self, body, title, meetup_id, createdBy):
        """Method that creates questions"""
        data = {
            "body":body,
            "title":  title,
            "meetup_id":  meetup_id,
            "createdBy": createdBy
        }

        try:
            add_question = "INSERT INTO \
                        questions (\
                                body,\
                                title,\
                                meetup_id,\
                                createdBy) \
                        VALUES ('" + body +"', '" + title +"', '" + meetup_id +"', '" + createdBy +"')"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_question, data)
            connect.commit()
            response = jsonify({'status': 201,
                                "msg":'Question Successfully Posted'})
            return response
            response.status_code = 201

        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'status': 400,
                                'error':'A database error occured'})
            response.status_code = 400
            return response

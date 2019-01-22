"""handles all operations for creating and fetching data relating to questions"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper
            
class Questions(Helper):
    """Class to handle questions"""
    def create_question(self, body, title, meetup_id, createdBy):
        """Method that creates questions"""
        present = Helper.check_if_meetup_id_exists(self, meetup_id)
        if not present:
                        return{
                                "status": 404,
                                "error": "Meetup ID to which you are posting on does not exist"
                            }, 404

        duplicate_question = Helper.check_if_similar_question_exists(self, title)
        if duplicate_question:
                        return{
                                "status": 401,
                                "error": "There is a question with the same conted already posted"
                            }, 401
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
            response = jsonify({'status': 500,
                                'error':'A database error occured'})
            response.status_code = 500
            return response

    def get_all_questions(self):
        """Method to get all questions"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
        return make_response(jsonify({
                "status": 200,
                "msg": "All posted questions",
                "data": questions
                }))

    def get_one_question(self, question_id):
        """Gets a particular meetup"""
        question = Helper.check_if_question_exists(self, question_id)
        if question:
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Question",
                    "data": question
                }))
        return make_response(jsonify( {
                    "status": 404,
                    "msg": "Question with that ID not found"
                }))
                
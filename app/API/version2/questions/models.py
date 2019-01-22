"""handles all operations for creating and fetching data relating to questions"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper



class Questions(Helper):
    """Class to handle questions"""
    def create_question(self, body, title, meetup_id, user_id):
        """Method that creates questions"""

        present = Helper.check_if_meetup_id_exists(self, meetup_id)
        if not present:
                        return{
                                "status": 404,
                                "error": "Meetup ID to which you are posting on does is not found"
                            }, 404

        duplicate_question = Helper.check_if_similar_question_exists(self, title)
        if duplicate_question:
                        return{
                                "status": 409,
                                "error": "There is a question with the same content already posted"
                            }, 409
        data = {
            "body":body,
            "title":  title,
            "meetup_id":  meetup_id,
            "user_id": user_id
        }

        try:
            add_question = "INSERT INTO \
                        questions (\
                                body,\
                                title,\
                                meetup_id,\
                                user_id) \
                        VALUES ('" + body +"', '" + title +"', '" + meetup_id +"', '" + user_id +"') returning *"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_question, data)
            connect.commit()
            question = cursor.fetchone()
            print(question)
            response = jsonify({'status': 201,
                                "msg":'Question Successfully Posted',
                                "data":self.quiz_json(question)})
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
                "data": [self.quiz_json(question) for question in questions]
                }))

    def get_one_question(self, question_id):
        """Gets a particular meetup"""
        question = Helper.check_if_question_posted_exists(self, question_id)
        if question:
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Question",
                    "data": self.quiz_json(question),
                    "comments":[]
                }))
        return make_response(jsonify( {
                    "status": 404,
                    "msg": "Question with that ID not found"
                }))

     
    def upvote_question(self, question_id):
        question = Helper.check_ques(self,question_id)
        if not question:
            return {"message": "That question does not exist"}, 404
        user_id = question[3]
        votes = question[6]
        if user_id:
            if votes > 0:
                return {"Message": "you can't vote again"}
        query = "UPDATE questions SET votes = votes + 1 WHERE question_id = '{}';".format(question_id)
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        cursor.execute("SELECT * FROM questions WHERE question_id=%(question_id)s",\
            {"question_id":question_id})
        result = cursor.fetchone()
        return make_response(jsonify({
                "status": 200,
                "msg": "Question",
                "data":self.quiz_json(result)
                }))

    def downvote_question(self, question_id):
        question = Helper.check_ques(self,question_id)
        if not question:
            return {"message": "That question does not exist"}, 404
        user_id = question[3]
        votes = question[6]
        if user_id:
            if votes > 0:
                return {"Message": "you can't vote again"}
        query = "UPDATE questions SET votes = votes - 1 WHERE question_id = '{}';".format(question_id)
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        cursor.execute("SELECT * FROM questions WHERE question_id=%(question_id)s",\
            {"question_id":question_id})
        result = cursor.fetchone()
        return make_response(jsonify({
                "status": 200,
                "msg": "Question",
                "data": self.quiz_json(result)
                }))
                
    def get_one_question_comments(self, question_id):
        question = question = Helper.check_ques(self,question_id)
        comments = self.get_by_criteria("comments", "question_id", question_id)
        if question:
            return make_response(jsonify({
                        "status": 200,
                        "msg": "question",
                        "data": self.quiz_json(question),
                        "comments": [Helper.comment_json(comments) for comment in comments]
                 }))
        

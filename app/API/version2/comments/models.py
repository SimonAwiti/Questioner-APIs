"""handles all operations for creating and fetching data relating to comments"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class Comments:
    """A class that handles all the comments operations"""

    def create_comment(self, user_id, question_id, title, comment):
        """Method to create a comment"""
        data = {
            "user_id": user_id,
            "question_id": question_id,
            "title": title,
            "comment": comment
        }
        try:
            add_comment = "INSERT INTO \
                        comments (\
                                user_id,\
                                question_id,\
                                title,\
                                comment) \
                        VALUES ('" + user_id +"', '" + question_id +"', '" + title +"', '" + comment +"')"

            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_comment, data)
            connect.commit()
             
            response = jsonify({'status': 201,
                                "msg":'Comment Successfully Posted'})
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'status': 500,
                                'error':'A database error occured'})
            response.status_code = 500
            return response

    def get_all_comments(self):
        """Method to get all comments"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM comments")
        comments = cursor.fetchall()
        return make_response(jsonify({
                "status": 200,
                "msg": "All posted comments",
                "data": [comments]
                }))
                
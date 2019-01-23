"""handles all operations for creating and fetching data relating to comments"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class Comments:
    """A class that handles all the comments operations"""
    @staticmethod
    def json(data):
        return dict(id=data[0],
        user_id=data[2],
        question_id=data[1],
        title=data[3],
        comment=data[4],
        createdOn=data[5]
        )

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
                        VALUES ('" + user_id +"', '" + question_id +"', '" + title +"', '" + comment +"') returning *"

            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_comment, data)
            connect.commit()
            comment = cursor.fetchone()
             
            response = jsonify({'status': 201,
                                "msg":'Comment Successfully Posted',
                                "data": Comments.json(comment) })
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
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
                "data": [Comments.json(comment) for comment in comments]
                }))
                
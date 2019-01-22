"""handles all operations for creating and fetching data relating to comments"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class Comments:
    """A class that handles all the comments operations"""

    def create_comment(self, question_id, title, comment):
        """Method to create a comment"""
        data = {
            "question_id": question_id,
            "title": title,
            "comment": comment
        }
        try:
            comment_query = """INSERT INTO
                        comments (question_id, title, comment)
                        VALUES (%s, %s, %s)"""
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(comment_query, data)
            connect.commit()
             
            response = cursor.fetchone()
            return jsonify({
                                'status': 201,
                                'data':[{
                                    'comment':response,
                        }]
                    }), 201
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'status': 500,
                                'error':'A database error occured'})
            response.status_code = 500
            return response

"""handles all operations for creating and fetching data relating to voting"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class QuestionsVotes(Helper):
    """Class to handle questions votting"""
    def downvote(self, question_id, user_id):
        try:
            conn = connection.dbconnection()
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor2.execute("SELECT * FROM downvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            downvoted = cursor2.fetchall()
            if downvoted:
                return make_response(jsonify(dict(error="You have already downvoted the question", status=409)))
            cursor.execute("SELECT * FROM upvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            vote = cursor.fetchall()
            if vote:
                cursor.execute("DELETE  FROM upvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            else:
                cursor.execute("INSERT INTO downvotes(question_id, user_id)VALUES(%d, %d) ON CONFLICT DO NOTHING"%(question_id, user_id))
            conn.commit()
            return make_response(jsonify(dict(message="You have successfully voted the question %d"%(question_id), status=201)))
        except(Exception, psycopg2.DatabaseError) as ex:
            return make_response(jsonify(dict(error="Something went wrong. Try again %d"%(question_id), status=500)))
    def upvote(self, question_id, user_id):
        try:
            conn = connection.dbconnection()
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor2.execute("SELECT * FROM upvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            upvoted = cursor2.fetchall()
            if upvoted:
                return make_response(jsonify(dict(error="You have already upvoted the question", status=409)))
            cursor.execute("SELECT * FROM downvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            vote = cursor.fetchall()
            if vote:
                cursor.execute("DELETE  FROM downvotes WHERE question_id=%d AND user_id=%d"%(question_id, user_id))
            else:
                cursor.execute("INSERT INTO upvotes(question_id, user_id)VALUES(%d, %d) ON CONFLICT DO NOTHING"%(question_id, user_id))
            conn.commit()
            return make_response(jsonify(dict(message="You have successfully upvoted the question %d"%(question_id), status=201)))
        except(Exception, psycopg2.DatabaseError) as ex:
            return make_response(jsonify(dict(error="Something went wrong. Try again %d"%(question_id), status=500)))
 
"""handles all operations for creating and fetching data relating to rsvps"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class Rsvps:
    """A class that handles all the comments operations"""

    def create_rsvp(self, user_id, meetup_id, response):
        """Method to create an rsvp"""
        data = {
            "user_id": user_id,
            "meetup_id": meetup_id,
            "response": response
        }
        try:
            add_rsvp = "INSERT INTO \
                        rsvps (\
                                user_id,\
                                comment_id,\
                                response) \
                        VALUES ('" + user_id +"', '" + meetup_id +"', '" + response +"')"

            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_rsvp, data)
            connect.commit()
             
            resp = jsonify({'status': 201,
                                "msg":'RSVP Successfully Posted'})
            return resp
            resp.status_code = 201

        except (Exception, psycopg2.DatabaseError) as error:
            resp = jsonify({'status': 500,
                                'error':'A database error occured'})
            resp.status_code = 500

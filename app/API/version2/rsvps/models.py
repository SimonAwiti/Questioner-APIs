"""handles all operations for creating and fetching data relating to rsvps"""
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request, jsonify, make_response
from datetime import datetime, timedelta

from app.API.utilities.database import connection
from app.API.version2.meetups.models import Helper

class Rsvps:
    """A class that handles all the comments operations"""

    @staticmethod
    def json(data):
        return dict(id=data[0],
        user_id=data[1],
        meetup_id=data[2],
        response=data[3]
        )

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
                                meetup_id,\
                                response) \
                        VALUES ('" + user_id +"', '" + meetup_id +"', '" + response +"') returning *"

            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_rsvp, data)
            connect.commit()
            rsvps = cursor.fetchone()
             
            resp = jsonify({'status': 201,
                                "msg":'RSVP Successfully Posted',
                                "data": Rsvps.json(rsvps)})
            return response
            response.status_code = 201

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            resp = jsonify({'status': 500,
                                'error':'A database error occured'})
            resp.status_code = 500
        return resp

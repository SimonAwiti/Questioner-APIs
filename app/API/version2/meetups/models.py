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
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            return {'error' : '{}'.format(error)}, 401
            
class Meetups(Helper):
    """Class to handle meetups"""
    def add_meetup(self, location, topic):
        """Method to handle user creation"""

        present = Helper.check_if_meetup_exists(self, topic)
        if present:
            return{
                "status": 401,
                "error": "There is a meetup with a similer topic"
                }, 401

        data = {
            "createdOn":str(datetime.now()),
            "location":  location,
            "topic":  topic,
            "happeningOn": str(datetime.now() + timedelta(days=10))
        }

        try:
            add_meetup = "INSERT INTO \
                        meetups (\
                                createdOn,\
                                location,\
                                topic,\
                                happeningOn) \
                        VALUES ('" + str(datetime.now()) +"', '" + location +"', '" + topic +"', '" + str(datetime.now() + timedelta(days=10)) +"')"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_meetup, data)
            connect.commit()
            response = jsonify({'status': 201,
                                "msg":'Meetup Successfully Created'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'status': 400,
                                'error':'A database error occured'})
            response.status_code = 400
            return response

    def get_all_meetups(self):
        """Method to get all meetups"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM meetups")
        meetups = cursor.fetchall()
        all_meetups = []
        for meetup in meetups:
            info = {meetup[0]: { "meetup_id": meetup[1],
                                 "createdOn": meetup[2],
                                 "location": meetup[3],
                                 "topic": meetup[4],
                                 "happeningOn": meetup[4]}}
            all_meetups.append(info)
        return make_response(jsonify({
                "status": 200,
                "msg": "All added meetups",
                "data": all_meetups
                }))

    def delete_meetups(self, meetup_id):
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM meetups WHERE meetup_id=%(meetup_id)s",\
            {"meetup_id":meetup_id})
        meetup = cursor.fetchall()
        if meetup:
            cursor.execute("DELETE FROM meetups WHERE meetup_id=%(meetup_id)s",\
                {'meetup_id':meetup_id})
            connect.commit()
            return make_response(jsonify({
                    "status": 202,
                    "msg": "Meetup succesfully deleted"
                }))
        return make_response(jsonify({
                    "status": 404,
                    "msg": "Meetup with that ID not found"
                }))

    def get_one_meetup(self, meetup_id):
        """Gets a particular meetup"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM meetups WHERE meetup_id=%(meetup_id)s",\
            {"meetup_id":meetup_id})
        meetup = cursor.fetchall()
        if meetup:
            return make_response(jsonify({
                    "status": 200,
                    "msg": "Meetup",
                    "data": meetup
                }))
        return make_response(jsonify( {
                    "status": 404,
                    "msg": "Meetup with that ID not found"
                }))
                
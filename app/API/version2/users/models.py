"""handles all operations for creating and fetching data relating to users"""
import psycopg2
from flask import request, jsonify


from flask import current_app
from app.API.utilities.database import connection


class Helper():
    """Carries out common functions"""
    def check_if_user_exists(self, email):
        """
        Helper function to check if a user exists
        Returns a message if a user already exists
        """
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM users WHERE email = '{}'".format(email))
            connect.commit()
            username = cursor.fetchone()
            cursor.close()
            connect.close()
            if username:
                return {'msg' : 'User already exists'}, 401
        except (Exception, psycopg2.DatabaseError) as error:
            return {'error' : '{}'.format(error)}, 401


class Users(Helper):
    """Class to handle users"""
    def reg_user(self, firstname, lastname, email, password, confirm):
        """Method to handle user creation"""
        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        confirm = request.json.get('confirm', None)

        # Check for empty inputs
        if firstname == '' or lastname == '' or email == '' or password == '' or confirm == '':
            return{
                "status": 401,
                "error": "Neither of the fields can be left empty"
                }, 401

        if password != confirm:
            return{
                "status": 401,
                "error": "The passwords do not match"
                }, 401


        if len(password) < 6 or len(password) > 12:
            return{
                "status": 401,
                "error": "Password length should be between 6 and 12 characters long"
                }, 401

        present = Helper.check_if_user_exists(self, email)
        if present:
            return{
                "status": 401,
                "error": "There is a user with the same email"
                }, 401

        try:
            add_user = "INSERT INTO \
                        users (firstname, lastname, email, password, confirm, admin) \
                        VALUES ('" + firstname +"', '" + lastname +"', '" + email +"', '" + password +"', '" + confirm +"', false )"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_user)
            connect.commit()
            response = jsonify({'status': 201,
                                "msg":'User Successfully Created'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'status': 400,
                                'msg':'Problem fetching record from the database'})
            response.status_code = 400
            return response

    def login_user(self, email, password):
        """Logs in a user"""
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        # Check for empty inputs
        if email == '' or password == '':
            return{
                "status": 401,
                "error": "Neither of the fields can be left empty during log in"
                }, 401

        try:
            get_user = "SELECT email, password, admin, user_id \
                        FROM users \
                        WHERE email = '" + email + "' AND password = '" + password + "'"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(get_user)
            row = cursor.fetchone()
            if row is not None:
                response = jsonify({"status":200,
                                    "msg":"User Successfully logged in"})
                response.status_code = 200
                return response
            response = jsonify({"status": 401,
                "msg" : "Error logging in, credentials not found"})
            response.status_code = 401
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'msg':'Problem fetching record from the database'})
            response.status_code = 400
            return response

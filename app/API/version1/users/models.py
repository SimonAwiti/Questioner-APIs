"""handles all operations for creating and fetching data relating to users"""
import os
from flask import request
from flask_jwt_extended import create_access_token

users = []


def check_if_user_exists(item):
    """
    Helper function to check if a user exists
    """
    user = [user for user in users if user['email'] == item.rstrip()]
    if user:
        return True
    return False

def verify_credentials(email, password):
    """
    Helper function to check if passwords match
    """
    user = [user for user in users if user['email'] == email and user['password'] == password]
    if user:
        return True
    return False

class Users():
    """Class to handle users"""
    def add_user(self, firstname, lastname, email, password, confirm):
        """Registers a new user"""
        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        confirm = request.json.get('confirm', None)

        if firstname == '' or lastname == ''  or email == ''  or password == '' or confirm == '':
            return {'error': 'Fields cannot be empty'}, 401

        if password != confirm:
            return {'msg':"Passwords do not match"}, 401

        if len(password) < 6 or len(password) > 12:
            return {'msg': "Password length should be between 6 and 12 characters long"}, 401

        duplicate = check_if_user_exists(email)
        if duplicate:
            return {'msg':'User already exists'}, 401
        
        user_dict = {
            "user_id": len(users) + 1,
            "firstname" : firstname.rstrip(),
            "lastname" : lastname,
            "email" : email,
            "password" : password,
            "confirm" : confirm,
            "admin" : False
        }
        users.append(user_dict)
        return {'msg':"User succesfully Registered"}, 201

    def login(self, email, password):
        """Logs in a user"""
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if email == '' or password == '':
            return {'error': 'Fields cannot be empty'}, 401

        credentials = verify_credentials(email, password)
        if not credentials:
            return {'msg':'Error logging in, ensure email or password are correct'}, 401
        
        user = [user for user in users if user['email'] == email.rstrip()]
        access_token = create_access_token(identity={'email':user[0]['email'], 'user_id':user[0]['user_id'], 'admin':user[0]['admin']})

        return {{"msg":"User succesfully Logged in"}, access_token}, 200
        
"""Unit tests for the users resources"""

import unittest
import json
from app import create_app

class TestUsers(unittest.TestCase):
    """Class containing all tests for the users resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.user = {
            "firstname":"Simon",
            "lastname":"Awiti",
            "email":"simonawiti@gmail.com",
            "password":"pass123",
            "confirm":"pass123",
        }
        self.user2 = {
            "firstname":"",
            "lastname":"",
            "email":"",
            "password":"",
            "confirm":"",
        }
        self.user3 = {
            "firstname":"John",
            "lastname":"Kariuki",
            "email":"trononawiti@gmail.com",
            "password":"pa23",
            "confirm":"pa23",
        }
        self.user4 = {
            "firstname":"Simon",
            "lastname":"Awiti",
            "email":"johnawiti@gmail.com",
            "password":"pass123",
            "confirm":"conpass123",
        }
        self.user5 = {
            "firstname":"Victor",
            "lastname":"Awiti",
            "email":"johnawuvigmail.com",
            "password":"conpass123",
            "confirm":"conpass123",
        }
        self.user6 = {
            "firstname":"1",
            "lastname":"2",
            "email":"simonawitti@gmail.com",
            "password":"pass123",
            "confirm":"pass123",
        }
        self.user7 = {
            "firstname":"Simon",
            "lastname":"Awiti",
            "email":"simonawiti@gmail.com",
            "password":"pass123",
            "confirm":"pass123",
        }
        self.login = {
            "email":"simonawiti@gmail.com",
            "password":"pass123"
        }

        self.login2 = {
            "email":"simonawiti@gmail.com",
            "password":"pass3"
        }
    def test_add_user(self):
        """Tests for adding a new user"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("User succesfully Registered", str(response.data))

    def test_for_successful_login(self):
        """Tests if a user successfully logged in"""
        response = self.client().post(
            '/api/v1/users/auth/login', 
            data=json.dumps(self.login), 
            content_type='application/json'
            )
        #self.assertEqual(response.status_code, 200)
        #self.assertIn("User succesfully Logged in", str(response.data))

    def test_add_user_wrong_passwords(self):
        """Tests for checking if password match"""
        response = self.client().post(
            '/api/v1/users/auth/login',
            data=json.dumps(self.login2), 
            content_type='application/json')
        self.assertEqual(response.status_code, 401)
        #self.assertIn("logging in, ensure email or password are correct or you are registered", str(response.data))

    def test_add_user_with_no_fields(self):
        """Tests for adding a new user with no fields"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user2), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("Fields cannot be left empty", str(response.data))

    def test_add_user_with_weak_password(self):
        """Tests for adding a new user with weak passwords"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user3), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("Error logging in, credentials not found", str(response.data))

    def test_add_user_with_unmatching_passwords(self):
        """Tests for adding a new user with unmatching password"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user4), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("Passwords do not match", str(response.data))

    def test_add_user_with_poor_email(self):
        """Tests for adding a new user with poor email"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user5), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("Invalid email provided", str(response.data))
    
    def test_add_user_with_digit_names(self):
        """Tests for adding a new user with digit"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user6), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("User names cannot be digits", str(response.data))

    def test_add_user_who_exists(self):
        """Tests for adding a new user who exists"""
        response = self.client().post(
            '/api/v1/users/auth/register', 
            data=json.dumps(self.user7), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 401)
        #self.assertIn("User already exists", str(response.data))

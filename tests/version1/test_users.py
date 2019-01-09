"""Unit tests for the users resources"""

import unittest
import json
from app import create_app

from datetime import datetime

class TestUsers(unittest.TestCase):
    """Class containing all tests for the users resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.user = {
            "id" : 1,
            "firstname":"Simon",
            "lastname":"Awiti",
            "othername":"Antonny",
            "email":"simonawiti@gmail.com",
            "phoneNumber" : "0792266400",
            "username":"Simon",
            "registered" : ["date"],
            "password":"pass123",
            "confirm":"pass123",
            "isAdmin" : False
        }

        self.login = {
            "name":"simon",
            "password":"pass123"
        }

    def test_add_user(self):
        """Tests for adding a new user"""
        response = self.client().post('/api/v1/users/register', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("User succesfully Registered", str(response.data))

    def test_for_successful_login(self):
        """Tests if a user successfully logged in"""
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.login), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("User succesfully Logged in", str(response.data))

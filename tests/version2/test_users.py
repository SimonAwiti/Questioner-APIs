"""Tests for handling the users resource"""
import unittest
import json

from app import create_app
from app.API.utilities.database import connection

class UserTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user = {
            "firstname" : "Ken", 
            "lastname" : "joseph", 
            "email" : "mysecret12@gmail.com",
            "password" : "joseph12",
            }
        self.user2 = {
            "firstname" : "simon", 
            "lastname" : "jose", 
            "email" : "myseuuret12@gmail.com",
            "password" : "joseph12",
            }
        with self.app.app_context():
            connection.dbconnection()
            connection.initializedb()
            connection.generate_admin()

    def tearDown(self):
        """Drops all tables after tests are done"""
        with self.app.app_context():
            connection.dbconnection()
            connection.drop_tables()

    def test_user_login(self):
        """Successfully log into the app"""
        response = self.client().post('/api/v2/auth/login',
                                      data=json.dumps(self.user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User Successfully logged in', str(response.data))

    def test_user_register(self):
        """Test to successfuly register a new user reg"""
        response = self.client().post('/api/v2/auth/signup',
                                      data=json.dumps(self.user2),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Successfully Created', str(response.data))

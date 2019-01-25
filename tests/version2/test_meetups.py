"""Tests for handling the meetups resource"""
import unittest
import json

from app import create_app
from app.API.utilities.database import connection

class MeetupsTestCase(unittest.TestCase):
    """Unit testiing for the meetups"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.admin = {
            "email" : "admin12@gmail.com",
            "password" : "passadmin",
            }
        self.meetup = {
            "location" : "Andela main hall",
            "topic" : "Proper HTML/CSS",
            }

        with self.app.app_context():
            connection.dbconnection()
            connection.initializedb()

    def tearDown(self):
        """Drops all tables after tests are done"""
        with self.app.app_context():
            connection.dbconnection()
            connection.drop_tables()

    def test_reg_user_deleting_of_meetup(self):
        """Test for deleting a meetup"""
        response = self.client().post('/api/v2/users/auth/login',
                                      data=json.dumps(self.admin),
                                      content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('User Successfully logged in', str(response.data))
        response = self.client().post('/api/v2/meetups',
                                      data=json.dumps(self.meetup),
                                      content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('Missing Authorization Header"', str(response.data))
        response = self.client().delete('/api/v2/meetups/1',
                                      data=json.dumps(self.meetup),
                                      content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('Missing Authorization Header', str(response.data))
        
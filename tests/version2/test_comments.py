"""Tests for handling the comments resource"""
import unittest
import json

from app import create_app
from app.API.utilities.database import connection

class CommentsTestCase(unittest.TestCase):
    """Unit testiing for the comments"""
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
        self.login1 = {
            "email" : "mysecret12@gmail.com",
            "password" : "joseph12",
            }

        self.user2 = {
            "firstname" : "simon", 
            "lastname" : "jose", 
            "email" : "myseuuret12@gmail.com",
            "password" : "joseph12",
            }
        self.comment1 = {
            "question_id" : "1", 
            "title" : "Git work flow", 
            "comment" : "such a nice question to be discussed",
            }
        self.meetup1 = {
            "location" : "Andela main hall",
            "topic" : "Streaming",
            }
        self.question1 = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "markup",
            "createdBy" : "joseph",
            "meetup_id" : 1,
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


    def test_comments_posting(self):
        """Test to successfuly add comments"""
        response = self.client().post('/api/v2/auth/signup',
                                      data=json.dumps(self.user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Successfully Created', str(response.data))
        response = self.client().post('/api/v2/auth/login',
                                      data=json.dumps(self.login1),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User Successfully logged in', str(response.data))

        response = self.client().post('/api/v2/meetups',
                                    data=json.dumps(self.meetup1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Meetup succesfully posted", str(response.data))

        response = self.client().post('/api/v2/questions',
                                    data=json.dumps(self.question1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Question succesfully posted", str(response.data))
        response = self.client().post('/api/v2/comments/1',
                                      data=json.dumps(self.comment1),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Comment Successfully Posted', str(response.data))
        
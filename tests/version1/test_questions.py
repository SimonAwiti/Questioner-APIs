"""Unit tests for the question resources"""

import unittest
import json
from app import create_app


class TestUsers(unittest.TestCase):
    """Class containing all tests for the question resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.question = {
            "createdOn" : ["date"],
            "createdby" : 3,
            "meetup" : 2,
            "title" : "Git workflow",
            "body" : "what is the best way of sorting merge conflict",
            "votes" : 20
        }
    def test_post_question(self):
        """Tests for posting a new question record"""
        response = self.client().post(
            '/api/v1/questions', 
            data=json.dumps(self.question), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Question succesfully posted", str(response.data))
        
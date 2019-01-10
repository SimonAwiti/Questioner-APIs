"""Unit tests for the meetups resources"""

import unittest
import json
from app import create_app

from datetime import date

class TestUsers(unittest.TestCase):
    """Class containing all tests for the meetups resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.meetup = {
            "createdOn" : ["date"],
            "location" : "Andela main hall",
            "topic" : "Git work flow at its best",
            "happeningOn" : ["date"],
            }

    def test_post_meetup(self):
        """Tests for posting a new meetup record"""
        response = self.client().post(
            '/api/v1/meetups', 
            data=json.dumps(self.meetup), 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Meetup succesfully posted", str(response.data))

    def test_get_specific_meetup(self):
        """Test for getting a specific meetup record"""
        response = self.client().get(
            '/api/vi/meetups/1',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Meetup record", str(response.data))

    def test_get_all_meetups(self):
        """Tests for getting all meetup records posted"""
        response = self.client().get(
            '/api/vi/meetups',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("All scheduled meetups", str(response.data))
        
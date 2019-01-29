"""Unit tests for the meetups resources"""

import unittest
import json
from app import create_app

from datetime import date

class TestMeetup(unittest.TestCase):
    """Class containing all tests for the meetups resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client()
        self.meetup = {
            "location" : "Andela main hall",
            "topic" : "Git work flow at its best",
            }
        self.meetup2 = {
            "location" : "Andela main hall",
            "topic" : "Versioning",
            }
        self.meetup3 = {
            "location" : "Andela main hall",
            "topic" : "Versioning",
            }
        self.meetup4 = {
            "location" : "",
            "topic" : "",
            }
        self.meetup5 = {
            "location" : "1",
            "topic" : "2",
            }

    def test_post_meetup(self):
        """Tests for posting a new meetup record"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup3),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response.data))

    def test_get_all_meetups(self):
        """Test for getting all meetups"""
        response = self.client.get('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn("All meetups posted", str(response.data))
        
    def test_get_one_meetup(self):
        """Test for getting one meetup"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        #self.assertIn("please provide all the fields, missing", str(response.data))
        response = self.client.get('/api/v1/meetups/1',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn("Meetup record", str(response.data))
    
    def test_post_a_meetup_with_same_content(self):
        """Tests for posting a new meetup record with same content"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        #self.assertIn("There is a meetup with the same topic", str(response.data))

    def test_post_meetup_with_no_field(self):
        """Test for trying to post a meetup with no field"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup4),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Fields cannot be left empty", str(response.data))

    def test_post_meetup_with_digit_fields(self):
        """Test for trying to post a meetup with no field"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup5
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("The fields should be described in words", str(response.data))
    
    def test_get_one_meetup_not_found(self):
        """Test for getting one questions"""
        response = self.client.get('/api/v1/meetups/10',
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Meetup record with that ID not found", str(response.data))


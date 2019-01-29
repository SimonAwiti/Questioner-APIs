import unittest
import json

from app import create_app

class TestRspv(unittest.TestCase):
    """Test case for the rsvp model"""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.meetup = {
            "location" : "Andela main hall",
            "topic" : "HTMLSCC",
            }
        self.meetup2 = {
            "location" : "Andela",
            "topic" : "MEETIINGS",
            }
        self.rsvp = {
            "response" : "Yes",
            "user_id" : 3,
            "meetup_id" : 4,
        }
        self.rsvp2 = {
            "response" : "Yes",
            "user_id" : 3,
            "meetup_id" : 30,
        }
        self.rsvp3 = {
            "response" : "",
            "user_id" : "",
            "meetup_id" : "",
        }
        self.rsvp4 = {
            "response" : "11",
            "user_id" : 2,
            "meetup_id" : 30,
        }
        self.rsvp5 = {
            "response" : "Yes",
            "user_id" : "joseph",
            "meetup_id" : "one",
        }
        self.rsvp6 = {
            "response" : "Yes",
            "user_id" : 2,
            "meetup_id" : 2,
        }
    def test_post_a_rspv(self):
        """Test if the post rsvp"""
        response1 = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response1.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response1.data))
        response = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("RSVP succesfully posted", str(response.data))

    def test_get_rsvp_for_meeting(self):
        """Test for getting one meeting rsvp"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response.data))
        response1 = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp6),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("RSVP succesfully posted", str(response1.data))
        response = self.client.get('/api/v1/rsvps/2',
                                  content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn("All posted RSVPS", str(response.data))

    def test_post_rsvp_with_no_meetup(self):
        """Test for trying to post an rsvp with no meetup"""
        response = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 404)
        #self.assertIn("MeetuP to which you are posting an RSVP is NOT found", str(response.data))

    def test_post_rsvp_with_no_field(self):
        """Test for trying to post an rsvp with no field"""
        response = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp3),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Fields cannot be left empty", str(response.data))

    def test_post_rsvp_with_digit_fields(self):
        """Test for trying to post an rsvp with no field"""
        response = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp4),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("The fields should be described in words", str(response.data))

    def test_post_rsvp_with_alphabet_meetup_id(self):
        """Test for trying to post an rsvp with no field"""
        response = self.client.post('/api/v1/rsvps',
                                    data=json.dumps(self.rsvp5),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("The fields requiring id should be integers", str(response.data))
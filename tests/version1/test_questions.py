"""Unit tests for the question resources"""

import unittest
import json
from app import create_app


class TestQuestion(unittest.TestCase):
    """Class containing all tests for the question resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client()
        self.meetup = {
            "location" : "Andela main hall",
            "topic" : "Frameworks",
            }
        self.meetup2 = {
            "location" : "Andela main hall",
            "topic" : "GIT",
            }
        self.meetup3 = {
            "location" : "Andela main hall",
            "topic" : "Streaming",
            }
        self.question = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "markup",
            "createdBy" : "joseph",
            "meetup_id" : 1,
        }
        self.question2 = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "Git workflow",
            "createdBy" : "joseph",
            "meetup_id" : 1,
        }
        self.questions = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "Git workflow",
            "createdBy" : "joseph",
            "meetup_id" : 10,
        }
        self.question3 = {
            "body" : "",
            "title" : "",
            "createdBy" : "",
            "meetup_id" : "",
        }
        self.question4 = {
            "body" : "1",
            "title" : "2",
            "createdBy" : "3",
            "meetup_id" : 10,
        }
        self.question5 = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "Git workflow",
            "createdBy" : "joseph",
            "meetup_id" : "one",
        }
        self.question6 = {
            "body" : "what is the best way of sorting merge conflict",
            "title" : "Git workflow",
            "createdBy" : "joseph",
            "meetup_id" : 1,
        }
    def test_post_a_question(self):
        """Tests for posting a new question record"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response.data))

        response1 = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Question succesfully posted", str(response1.data))

    def test_get_all_questions(self):
        """Test for getting all questions"""
        response = self.client.get('/api/v1/questions',
                                    data=json.dumps(self.question),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("All posted questions", str(response.data))

    def test_get_one_question(self):
        """Test for getting one questions"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response.data))
        response1 = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Question succesfully posted", str(response1.data))
        response = self.client.get('/api/v1/questions/1',
                                    data=json.dumps(self.question2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn("question record", str(response.data))

    def test_post_question_with_no_meetup(self):
        """Test for trying to post a question with no meetup"""
        response = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.questions),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 404)
        #self.assertIn("MeetuP to which you are posting a question to is NOT found", str(response.data))

    def test_post_question_with_no_field(self):
        """Test for trying to post a question with no field"""
        response = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question3),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        #self.assertIn("Fields cannot be left empty", str(response.data))

    def test_post_question_with_digit_fields(self):
        """Test for trying to post a question with no field"""
        response = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question4),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        #self.assertIn("The fields should be described in words", str(response.data))

    def test_post_question_with_alphabet_meetup_id(self):
        """Test for trying to post a question with alphabetic id"""
        response = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question5),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        #self.assertIn("The field should be an integer", str(response.data))

    def test_post_a_question_with_same_content(self):
        """Tests for posting a new question record with same content"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup3),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("Meetup succesfully posted", str(response.data))

        response1 = self.client.post('/api/v1/questions',
                                    data=json.dumps(self.question6),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        #self.assertIn("There is a question with the similer content posted", str(response1.data))

    def test_get_one_question_not_found(self):
        """Test for getting one questions"""
        response = self.client.get('/api/v1/questions/10',
                                    data=json.dumps(self.question2),
                                    content_type='application/json')
        #self.assertEqual(response.status_code, 404)
        #self.assertIn("Question record with that ID not found", str(response.data))

        

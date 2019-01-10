"""handles all operations dealing with meetups"""

from flask import request, jsonify

from datetime import datetime, timedelta

# List to hold all the meetups to be posted
meetups = []

def check_if_meetup_exists(item):
    """
    Helper function to check if a meetup record already exists
    Returns True if meetup record already exists, else returns False
    """
    meetup = [meetup for meetup in meetups if meetup['topic'] == item.rstrip()]
    if meetup:
        return True
    return False

class Meetups():
    """Class to handle the meetup operations """

    def add_meetup(self, location, topic):
        """Add a product to the products list"""

        # Get the JSON object values
        #createdOn = datetime.now
        location = request.json.get('location', None)
        topic = request.json.get('topic', None)
        #happeningOn = datetime.now() + timedelta(days=5)

        if location == '' or topic == '':
            return {'error': 'Fields cannot be empty'}, 401 

        # Check for duplicate meetups
        present = check_if_meetup_exists(topic)
        if present:
            return {'msg':'There is a meetup with the same topic'}, 401
        
        # Add all attributes to a meetup dictionary
        meetup_dict={
            "id": len(meetups) + 1,
            "createdOn" : str(datetime.now()),
            "location" : location,
            "topic" : topic,
            "happeningOn" : str(datetime.now() + timedelta(days=5))
        }
        # Append to the meetup list
        meetups.append(meetup_dict)
        return {"msg": "Meetup succesfully posted"}, 201

    def get_all_meetups(self):
        """Fetch all meetup records from the meetup list"""
        # If meetup list is empty
        if len(meetups) == 0:
            return {'msg':'No Meetups added yet'}, 404
        return {'All scheduled meetups':meetups}, 200
    
    def get_one_meetup(self, meetup_id):
        """Fetches a specific meetup from the meetup list"""
        meetup = [meetup for meetup in meetups if meetup['id'] == meetup_id]
        if meetup:
            return {'Meetup record': meetup[0]}, 200
        # no meetup found
        return {'msg':'Meetup record with that ID not found'}, 404
        
import re
from datetime import datetime

def validate_meetups(args):
    """validate meetup details"""
    try:
        if any([(arg.strip() == '') for arg in args]):
            return{
                "status": 401,
                "error": "Fields cannot be left empty"
                }, 401
        elif( args["location"].isdigit()) or ( args["topic"].isdigit()) :
            return{
                "status": 401,
                "error": "The fields should be described in words"
                }, 401
        dates = args['happeningOn']
        try:
            happenning = datetime.strptime(dates, "%d/%m/%Y")
        except ValueError as exception:
            return {}
        days = (happenning - datetime.utcnow()).days
        if days < 0:
            return{
                "status": 401,
                "error": "Your happening date must be ahead of date of meetup posting"
                    }, 401
        return"valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401


def validate_rsvps(args):
    """validate rsvp details"""
    try:
        if args["response"] == '' or \
           args["user_id"] == '' or \
           args["meetup_id"] == '':
           return{
                "status": 401,
                "error": "Fields cannot be left empty"
                }, 401
        elif (args["response"]. isdigit()):
            return{
                "status": 401,
                "error": "The fields should be described in words"
                }, 401
        elif(args["meetup_id"]. isalpha()) or (args["user_id"]. isalpha()):
            return{
                "status": 401,
                "error": "The fields requiring id should be integers"
                }, 401
        elif (args["response"] != "yes"):
            return{
                "status": 401,
                "error": "The response should either be yes, no or maybe..."
                }, 401
        else:
            return "valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401

def validate_questions(args):
    """validate question details"""
    try:
        if args["body"] == '' or \
           args["title"] == '' or \
           args["meetup_id"] == '' :
           return{
                "status": 401,
                "error": "Fields cannot be left empty"
                }, 401
        elif(args["body"]. isdigit()) or \
            (args["title"]. isdigit()):
            return{
                "status": 401,
                "error": "The fields should be described in words"
                }, 401
        elif(args["meetup_id"]. isalpha()):
            return{
                "status": 401,
                "error": "The field should be an intege"
                }, 401
        else:
            return "valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401


def validate_comments(args):
    """validate comments details"""
    try:
        if args["question_id"] == '' or \
           args["title"] == '' or \
           args["comment"] == '' :
           return{
                "status": 401,
                "error": "Fields cannot be left empty"
                }, 401
        elif(args["title"]. isdigit()) or \
            (args["comment"]. isdigit()):
            return{
                "status": 401,
                "error": "The fields should be described in words"
                }, 401
        elif(args["question_id"]. isalpha()):
            return{
                "status": 401,
                "error": "The field should be an integer"
                }, 401
        else:
            return "valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401
                    



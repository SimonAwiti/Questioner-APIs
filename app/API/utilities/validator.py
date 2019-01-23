def validate_meetups(args):
    """validate meetup details"""
    try:
        if args["location"] == '' or args["topic"] == '':
            return {'error': 'Fields cannot be left empty'}, 401
        elif( args["location"]. isdigit()) or ( args["topic"]. isdigit()) :
            return {"error":"The fields should be described in words"},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

def validate_rsvps(args):
    """validate rsvp details"""
    try:
        if args["response"] == '' or \
           args["user_id"] == '' or \
           args["meetup_id"] == '':
            return {'error': 'Fields cannot be left empty'}, 401
        elif (args["response"]. isdigit()):
                return {"error":"The fields should be described in words"},401
        elif(args["meetup_id"]. isalpha()) or (args["user_id"]. isalpha()):
            return {"error":"The fields requiring id should be integers"},401
        elif (args["response"] != "yes"):
            return {"error":"The response should either be yes, no or maybe..."},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

def validate_questions(args):
    """validate question details"""
    try:
        if args["body"] == '' or \
           args["title"] == '' or \
           args["meetup_id"] == '' :
            return {'error': 'Fields cannot be left empty'}, 401
        elif(args["body"]. isdigit()) or \
            (args["title"]. isdigit()):
                return {"error":"The fields should be described in words"},401
        elif(args["meetup_id"]. isalpha()):
            return {"error":"The field should be an integer"},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

def validate_comments(args):
    """validate comments details"""
    try:
        if args["question_id"] == '' or \
           args["title"] == '' or \
           args["comment"] == '' :
            return {'error': 'Fields cannot be left empty'}, 401
        elif(args["title"]. isdigit()) or \
            (args["comment"]. isdigit()):
                return {"error":"The fields should be described in words"},401
        elif(args["question_id"]. isalpha()):
            return {"error":"The field should be an integer"},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)


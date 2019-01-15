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
        if args["topic"] == '' or \
           args["status"] == '' or \
           args["createdBy"] == '' or \
           args["meetup_id"] == '':
            return {'error': 'Fields cannot be left empty'}, 401
        elif(args["topic"]. isdigit()) or \
            (args["status"]. isdigit()) or \
            (args["createdBy"]. isdigit()):
                return {"error":"The fields should be described in words"},401
        elif(args["meetup_id"]. isalpha()):
            return {"error":"The field should be an integer"},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

def validate_questions(args):
    """validate question details"""
    try:
        if args["body"] == '' or \
           args["title"] == '' or \
           args["meetup_id"] == '' or \
           args["createdBy"] == '':
            return {'error': 'Fields cannot be left empty'}, 401
        elif(args["body"]. isdigit()) or \
            (args["title"]. isdigit()) or \
            (args["createdBy"]. isdigit()):
                return {"error":"The fields should be described in words"},401
        elif(args["meetup_id"]. isalpha()):
            return {"error":"The field should be an integer"},401
        else:
            return "valid"
    except Exception as error:
        return "please provide all the fields, missing " + str(error)

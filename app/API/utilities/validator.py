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


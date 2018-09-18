import json
from uuid import uuid4
from flask import Response


def get_unique_id():
    """
    Generates a unique ID.
    """
    unique_id = str(uuid4())
    return unique_id


def http_response(status_code, msg):
    """
    sends an http response to the user along with an error message   
    """
    return Response(json.dumps(msg), status_code, mimetype='application/json')

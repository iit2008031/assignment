import json
from uuid import uuid4
from flask import Response
from constants import cyrillic_translit


def get_unique_id():
    """
    Generates a unique job ID.
    """
    unique_id = str(uuid4())
    return unique_id


def http_response(status_code, msg):
    """
    sends an http response to the user along with an error message   """

    return Response(json.dumps(msg), status_code, mimetype='application/json')


def transliterate(word):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in cyrillic_translit:
            transchar = cyrillic_translit[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word

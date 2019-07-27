from functools import  wraps
from flask import request , g, abort ,session
import  json

def loginrequired(f):
    @wraps(f)
    def wrap(*args ,**kwargs):
        if 'username' not in session:
            return json.dumps({'error': 'invalid authorization token'}), 401, {'Content-type': 'application/json'}

        return f(*args , **kwargs)

    return  wrap

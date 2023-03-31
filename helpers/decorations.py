import jwt

from flask import request, abort
from helpers.constants import PWD_ALGORITHM, PWD_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split("Bearer ")[-1]
        try:
            jwt.decode(token, PWD_SECRET, algorithms=[PWD_ALGORITHM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper

from flask import Flask
from flask_jwt import JWT, current_identity
from werkzeug.security import safe_str_cmp


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

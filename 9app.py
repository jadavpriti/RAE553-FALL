from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id
users = [
    User(1, 'priti', 'abcxyz')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'priti'
api = Api(app)

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

items = {"piano" : {"price":20.00}}

parser = reqparse.RequestParser()
parser.add_argument('price')

class item(Resource):
    @jwt_required()
    def get(self, name):
        return items



    @jwt_required()
    def delete(self, name):
        del items
        return ''

    @jwt_required()
    def put(self, name):
        return items

    @jwt_required()
    def post(self, name):
            return items
        else:
            abort(404)

# ItemList
class items(Resource):
    def get(self):
        return items


##
## Actually setup the Api resource routing here
##
api.add_resource(itemList, '/items')
api.add_resource(item, '/items/<name>')


if __name__ == '__main__':

    app.run()

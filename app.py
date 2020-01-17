from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_jwt import JWT, jwt_required
from user import userRegister

from security import authenticate, identity
app = Flask(__name__)
app.secret_key = 'priti'
api = Api(app)
jwt = JWT(app, authenticate, identity)
items = {"piano":{"price":20},"test1":{"price":10},"test2":{"price":20},"test3":{"price":30}}


class items(Resource):
    @jwt_required()
    def get(self, name):
        if name not in items:
            items[name] = {"price": ""}
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[name]['price'] = args['price']
        return items[name]
    def put(self, name):
        if name not in items:
            items[name] = {"price": ""}
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[name]['price'] = args['price']
        return items[name]
    def delete(self, name):
        if name not in items:
            items[name] = {"price": ""}
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[name]['price'] = args['price']
        return items[name]
    def post(self, name):
        if name in items:
            parser = reqparse.RequestParser()
            parser.add_argument("price")
            args = parser.parse_args()
            items[name]['price'] = args['price']
            return items[name]
        else:
            return "Error {} name is not in items".format(type_name)
api.add_resource(items, '/items') #http://127.0.0.1:5000/items
api.add_resource(item, '/items/<name>') #http://127.0.0.1:5000/name
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':

    app.run()

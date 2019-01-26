# @author: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# @last_edited: 26/01/19
# @repo: https://github.com/aj-fernandez/

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "agustin",
        "age": 33,
        "occupation": "CIO"
    },
    {
        "name": "javier",
        "age": 34,
        "occupation": "CEO"
    },
    {
        "name": "victor",
        "age": 36,
        "occupation": "Engineer"
    },
    {
        "name": "marta",
        "age": 38,
        "occupation": "HHRR"
    }
]

class User(Resource):

    def get(self,name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User {} not found".format(name), 404

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        for user in users:
            if (name == user["name"]):
                return "User with name {} already exist".format(name), 400
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        users.append(user)
        return user, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self,name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
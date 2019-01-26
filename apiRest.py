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

    def post(self,name):
    
    def put(self,name):
    
    def delete(self,name):
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

import pandas as pd, ast
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('id', required = False)
        parser.add_argument('player', required = False)
        parser.add_argument('team', required = False)

        args = parser.parse_args()
        
        data = pd.read_csv('data.csv')
        data = data.to_dict()
        return {'data': data}, 200
    
    def post(self):
        return {'message': 'Action not allowed.'}, 405
    
    def put(self):
        return {'message': 'Action not allowed.'}, 405
    
    def delete(self):
        return {'message': 'Action not allowed.'}, 405

class Teams(Resource):
    pass

api.add_resource(Players, '/players')
api.add_resource(Teams, '/teams')

if __name__ == '__main__':
    app.run(debug=True)
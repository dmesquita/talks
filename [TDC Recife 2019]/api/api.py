import json
import sqlite3

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

from text_similarity_model.model import Model
from database import Database

app = Flask(__name__)
api = Api(app)

db = Database()

model = Model.deserialize("../models/model_1.0.0.pkl")
version = model.version

parser = reqparse.RequestParser()
parser.add_argument("title", required=True)
parser.add_argument("description", required=True)
parser.add_argument("n_results", required=False)

class Version(Resource):
    def get(self):
        return jsonify({"model_version": version})

class Predict(Resource):
    def post(self):
        palestras = None
        args = parser.parse_args()
        title = args["title"]
        description = args["description"]

        n_results = 3
        if args["n_results"]:
            print(args["n_results"])
            n_results = int(args["n_results"])

        data_to_predict = {"title":title,"description":description}
        db.save((title,description, version))

        palestras = model.predict(X=data_to_predict,
                                    n_results=n_results)
        
        return palestras

api.add_resource(Version, "/version")
api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=False)

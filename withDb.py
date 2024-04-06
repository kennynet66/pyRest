from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort

import uuid

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///database.db'


"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class productModel(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    desc = db.Column(db.String(1000), nullable = False)

    def __repr__(self):
        return f"Product(name = {name}, price = {price}, desc = {desc})"
"""



createProductArgs = reqparse.RequestParser()
createProductArgs.add_argument("name", type=str, help="Product name is required", required=True)
createProductArgs.add_argument("price", type=int, help="Price name is required", required=True)
createProductArgs.add_argument("desc", type=str, help="Description name is required", required=True)

products = {}

def abort_ifNotExists(productId):
    if productId not in products:
        abort(404, message = "Product doesn't exist")

def generateId():
    return str(uuid.uuid4())

class Products(Resource):
    def put(self):
        productId = generateId()
        args = createProductArgs.parse_args()
        products[productId] = args
        return {"success": "Product created successfully", "productId": productId}, 200

    def get(self):
        return products


api.add_resource(Products, "/products")

if __name__ == ("__main__"):
    app.run(debug=True)

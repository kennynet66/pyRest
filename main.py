from flask import Flask
from flask_restful import Api, Resource
import pyodbc


server = "DESKTOP-RRC62LG\\KENNY"
database = "Shopie"
username = "sa"
password = "Boomplay@1"

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

app = Flask(__name__)
api = Api(app)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    print("Connected to sqlserver")
        

except pyodbc.Error as e:
    print("Error connecting to the database", e)


class Products(Resource):
    def get(self):
        try:
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()

            # Convert each row to a dictionary
            products = []
            for row in rows:
                products.append(dict(zip([column[0] for column in cursor.description], row)))

            return {"products"}
        except pyodbc.Error as e:
            print("Error fetching products", e)


api.add_resource(Products, "/products")

if __name__ == "__main__":
    app.run(debug=True)
from email.mime import application
import json
from pickle import APPEND
from flask import Flask, abort, request  # Django
from about_me import me
from mock_data import catalog  # IMPORTANT STEP
from config import db
from bson import ObjectId

app = Flask('blueberry')


@app.route("/", methods=['GET'])  # root
def home():
    return "This is the home page"

# Create an about endpoint and show your name


@app.route("/about")
def about():
    return f"{me['first']} {me['last']}"  # return me["first"] + " " + ["last"]


@app.route("/myaddress")
def address():
    return f'  {me["address"]["number"]} {me["address"]["street"]}'


# JSON - JaveScript Object Notation API - Application Program Interface
############################################################################################# API ENDPOINTS ##################################################################################################
# Postman -> Test endpoints of REST APIs

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    results = []
    cursor = db.products.find({}) # get all data from the collection

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)

# POST Method to create new products
@app.route("/api/catalog", methods=["POST"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)

# make an endpoint to send back how mant product do we have in the catalog


@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    cursor = db.products.find({})
    num_items = 0
    for prod in cursor:
        num_items += 1
    # Here... count how many products are in the list catalog
    # counts = len(catalog)

    return json.dumps(num_items)  # return the value

# Request 127.0.0.1:5000/api/product/5f40a6baac77a903d8f682c6


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    # find the product whose _id is equal to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    # catalog
    # travel calatlog with for loop
    # get every product inside the list
    # if the _id of the prodcut is equal to the id variable
    # found it, return that product as JSON

    # return an error code
    return abort(404, "Id does not match any product")


# Create an endpoint that returns the SUM of all the products' price
# GET /api/catalog/total
# @app.route("/api/catalog/total", methods=["GET"])
@app.get('/api/catalog/total')
def get_total():
    cursor = db.products.find({})
    total = 0
    for prod in cursor:
        total += prod["price"]#total = total + prod["price"]
    return json.dumps(total)


# get product by category
# get /api/products/<category>

@app.get('/api/products/<category>')
def products_by_category(category):
    results = []
    category = category.lower()
    for prod in catalog:
        if prod['category'].lower() == category:
            results.append(prod)

    return json.dumps(results)

# get the list of categories
# get /api/categories


@app.get('/api/categories')
def get_unique_categories():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        cat = prod['category']
        # if cat does not exist in results, then
        if not cat in results:
            results.append(cat)
    
    return json.dumps(results)


# get the cheapest product
@app.get('/api/products/cheapest')
def get_cheapest_product():
    cursor = db.products.find({})
    solution = cursor[0]
    
    for prod in cursor:
        if prod['price'] < solution['price']:
            solution = prod
    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)


@app.get("/api/exercise1")
def get_exe1():
    nums = [123, 123, 654, 124, 8865, 532, 4768, 8476, 45762,
            345, -1, 234, 0, -12, -456, -123, -865, 532, 4768]
    solution = {}

    # A: print the lowest number
    solution['a'] = 1
    # B: count and print how many numbers are lower than 500
    solution['b'] = 1
    # sum all the negatives
    solution['c'] = 1
    # find the sum of numbers except negatives
    solution['d'] = 1

    return json.dumps(solution)


app.run(debug=True)

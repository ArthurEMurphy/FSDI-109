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
    try: 
        product = request.get_json()
        errors = ""

        # title, 5 chars long
        if not "title" in product or len(product["title"]) < 5:
            errors = (400, "Title is required")

        # must have an image
        if not "imgage" in product:
            errors += "", "Image is required"

        # must have a price, the price must be greater/equal to 1
        if not "price" in product or product["price"] < 1:
            errors += ", Price is required and should be greater than or equal to 1"

        if errors:
            return abort(400, errors)

        db.products.insert_one(product)
        product["_id"] = str(product["_id"])

        return json.dumps(product)

    except Exception as ex:
        return abort(500, "Unexpected Error {ex}")

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
    try:
        if not ObjectId.is_valid(id):
            return abort(400, "Invalid id")

        product = db.products.find_one({"_id": ObjectId(id)})

        if not product:
            abort(404, "Product not found")

        product["_id"] = str(product["_id"])
        return json.dumps(product)
    
    except:
        return abort(500, "Unexpected Error")

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
    cursor = db.products.find({"category": category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
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


################################################## COUPON CODES ########################################################
# get all
@app.route("/api/coupons", methods=["GET"])
def get_all_coupons():
    cursor = db.coupons.find({})
    results = []
    for cc in cursor:
        cc["_id"] = str(cc["_id"])
        results.append(cc)

    return json.dumps(results)

# save coupon codes
@app.route("/api/coupons", methods=["post"])
def save_coupon():
    coupon = request.get_json()

    # validations

    db.coupons.insert_one(coupon)

    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)

# get CC by code
@app.route("/api/coupons", methods=["GET"])
def get_coupon_by_Code(coupons):
    results = []
    cursor = db.coupons.find({"cc": coupons})
    for cc in cursor:
        cc["_id"] = str(cc["_id"])
        results.append(cc)

    return json.dumps(results)

app.run(debug=True)

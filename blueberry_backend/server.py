#from email.mime import application
import json
#from pickle import APPEND
from flask import Flask, Response, abort, request  # Django
from about_me import me
from mock_data import catalog  # IMPORTANT STEP
from config import db
from bson import ObjectId
from flask_cors import CORS

app = Flask('blueberry')
CORS(app)

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



# make an endpoint to send back how many products do we have in the catalog
@app.route("/api/catalog/count", methods=["GET"])
def get_count():# Here... count how many products are in the list catalog
    cursor = db.products.find({})
    num_items = 0
    for prod in cursor:
        num_items += 1

    return json.dumps(num_items)  # return the value


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    try:
        if not ObjectId.is_valid(id):
            return abort(400, "Invalid id")

        product = db.products.find_one({"_id": ObjectId(id)})

        if not product:
            return abort(404, "Product not found")

        product["_id"] = str(product["_id"])
        return json.dumps(product)
    
    except:
        return abort(500, "Unexpected Error")


@app.get('/api/catalog/total')
def get_total():
    total = 0
    cursor = db.products.find({})
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
    nums = [123, 123, 654, 124, 8865, 532, 4768, 8476, 45762, 345, -1, 234, 0, -12, -456, -123, -865, 532, 4768]
    solution = {}

    # A: print the lowest number
    solution['a'] = 1


    # B: count and print how many numbers are lower than 500
    solution['b'] = 1

    # C: sum all the negatives
    solution['c'] = 1
    
    
    # D: find the sum of numbers except negatives
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
@app.route("/api/coupons", methods=["POST"])
def save_coupon():
    try:
        coupon = request.get_json()

        # validations
        errors = ""
        if not "code" in coupon or len(coupon["code"]) < 5:
            errors += "Coupon should have at least 5 characters,"
            
        if not "discount" in coupon or coupon["discount"] < 1 or coupon["discount"] > 50:
            errors += "Dicount is required and should be between 1 and 50,"
        
        if errors:
            return Response(errors, status=400)

        # do not allow duplicate code
        exist = db.coupons.find_one({"code": coupon["code"]})
        if exist:
            return Response( "A coupon already exists for that Code", status=400 )

        db.coupons.insert_one(coupon)

        coupon["_id"] = str(coupon["_id"])
        return json.dumps(coupon)
    
    except Exception as ex:
        print(ex)
        return Response("Unexpected error", status=500)

# get CC by code
@app.route("/api/coupons/<code>", methods=["GET"])
def get_coupon_by_Code(code):
    
    coupon = db.coupons.find_one({"code": code})
    if not coupon:
        return abort(404, "Coupon not found")

    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)

app.run(debug=True)

from flask import Flask, request

from db import Base, engine
from resources.product import Product

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


# @app.route('/accounts/update_account', methods=['PUT'])
# def update_account():
#     account_id = request.args.get('account_id')
#     body = request.get_json()
#     return Account.update_account(account_id, body)


@app.route('/products/get_recommender_data', methods=['GET'])
def get_recommender_data():
    return Product.get_recommendation_data()


@app.route('/products/get_product', methods=['GET'])
def get_product():
    product_id = request.args.get('product_id')
    return Product.get(product_id)


@app.route('/products/register_product', methods=['POST'])
def register_product():
    req_data = request.get_json()
    return Product.register_product(req_data)


@app.route('/products/update_quantity_price', methods=['PUT'])
def update_quantity_price():
    product_id = request.args.get('product_id')
    req_data = request.get_json()
    return Product.update_quantity_price(product_id, req_data)


@app.route('/products/delete_product', methods=['DELETE'])
def delete_product():
    product_id = request.args.get('product_id')
    return Product.delete(product_id)

app.run(host='0.0.0.0', port=5000)

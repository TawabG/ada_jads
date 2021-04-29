from flask import Flask, request
from db import Base, engine
from resources.product import Product

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/products/get_recommender_data', methods=['GET'])
def get_recommender_data():
    return Product.get_recommendation_data()

@app.route('/products/register_product', methods=['POST'])
def register_product():
    req_data = request.get_json()
    return Product.create(req_data)

@app.route('/products/get_product/<p_id>', methods=['GET'])
def get_product(p_id):
    return Product.get(p_id)

@app.route('/products/update_quantity_price/<p_id>', methods=['PUT'])
def update_quantity_price(p_id):
    req_data = request.get_json()
    product_quantity = req_data['product_quantity']
    unit_price = req_data['unit_price']
    return Product.update(p_id, product_quantity, unit_price)

@app.route('/products/delete_product/<p_id>', methods=['DELETE'])
def delete_product(p_id):
    return Product.delete(p_id)

app.run(host='0.0.0.0', port=5000)

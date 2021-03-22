from flask import Flask, request
from db import Base, engine
from resources.cart import Cart

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/cart', methods=['POST'])
def create():
    req_data = request.get_json()
    return Cart.create(req_data)


@app.route('/cart/<c_id>', methods=['GET'])
def get(c_id):
    return Cart.get(c_id)


@app.route('/cart/<c_id>/<quantity>', methods=['PUT'])
def update(c_id, quantity):
    product_quantity = request.args.get('product_quantity')
    return Cart.update(c_id, quantity)


@app.route('/cart/<c_id>', methods=['DELETE'])
def delete(c_id):
    return Cart.delete(c_id)


app.run(host='0.0.0.0', port=5000)
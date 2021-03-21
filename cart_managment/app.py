from flask import Flask, request

from db import Base, engine
from resources.cart import Cart
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/cart', methods=['POST'])
def create_cart():
    req_data = request.get_json()
    return Cart.create(req_data)


@app.route('/cart/<c_id>', methods=['GET'])
def get_cart(c_id):
    return Cart.get(c_id)


@app.route('/cart/<c_id>', methods=['DELETE'])
def delete_cart(c_id):
    return Cart.delete(c_id)


app.run(host='0.0.0.0', port=5000)
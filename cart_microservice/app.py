from flask import Flask, request

from db import Base, engine
from resources.cart import Cart

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/cart', methods=['POST'])
def add_to_cart():
	req_data = request.get_json()
	return Cart.create(req_data)

@app.route('/cart/<cart_user_id>', methods=['GET'])
def get_cart_item(cart_user_id):
	return Cart.get(cart_user_id)

@app.route('/cart/<cart_user_id>/<product_id>/<quantity>', methods=['PUT'])
def update(cart_user_id, product_id, quantity):
	# product_quantity = request.args.get('product_quantity')
	return Cart.update(cart_user_id, product_id, quantity)


@app.route('/cart/<cart_user_id>', methods=['DELETE'])
def delete(cart_user_id):
    return Cart.delete(cart_user_id)


app.run(host='0.0.0.0', port=5000)

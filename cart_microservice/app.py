from flask import Flask, request

from db import Base, engine
from resources.cart import Cart

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/cart/add_to_cart', methods=['POST'])
def add_to_cart():
	req_data = request.get_json()
	return Cart.create(req_data)


@app.route('/cart/get_cart_items', methods=['GET'])
def get_cart_items():
	user_id = request.args.get('user_id')
	return Cart.get(user_id)


@app.route('/cart/update_cart', methods=['PUT'])
def update():
	user_id = request.args.get('user_id')
	req_data = request.get_json()
	return Cart.update(user_id, req_data)


@app.route('/cart/delete_cart', methods=['DELETE'])
def delete():
	user_id = request.args.get('user_id')
	return Cart.delete(user_id)


app.run(host='0.0.0.0', port=5000)

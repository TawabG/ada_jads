from flask import Flask, request

from db import Base, engine
from resources.cart import Cart

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/cart', methods=['POST'])
def add_to_cart():
	req_data = request.get_json()
	print(req_data)
	return Cart.create(req_data)

@app.route('/cart/<cart_user_id>', methods=['GET'])
def get_cart_item(cart_user_id):
	return Cart.get(cart_user_id)


# @app.route('/Cart/<c_id>/status', methods=['PUT'])
# def update_delivery_status(c_id):
#     status = request.args.get('status')
#     return Status.update(c_id, status)


# @app.route('/Cart/<c_id>/status/<c_id>', methods=['DELETE'])
# def delete_delivery(c_id):
#     return Cart.delete(c_id)


app.run(host='0.0.0.0', port=5000)

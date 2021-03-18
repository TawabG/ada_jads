from flask import jsonify
from daos.cart_dao import CartDAO
# import json
import simplejson as json

from db import Session

class Cart:
	@staticmethod
	def create(body):
		session = Session()
		cart = CartDAO(body['cart_user_id'], body['product_id'], body['product_name'], body['product_price'], 'static short description', '/product/path', 'path/to/img', body['amount'])
 
		session.add(cart)
		session.commit()
		session.refresh(cart)
		session.close()
		#return jsonify({'Product added to cart!': "Product added to cart!"}), 200
		return jsonify({'Succes!': f'Product with name: {cart.product_name} has been added to the cart.'}), 200


	@staticmethod
	def get(cart_user_id):
		session = Session()

		# compare cart_user_id in database with cart_user_id of json body
		cart = session.query(CartDAO).filter(CartDAO.cart_user_id == cart_user_id).all()

		# check if cart_user_id exists (thus if an item is in the cart)
		if cart:
			# if so, return all items in cart
			list_return = [] 
			for item in session.query(CartDAO).filter(CartDAO.cart_user_id == cart_user_id).all():
				dictret = dict(item.__dict__)
				dictret.pop('_sa_instance_state', None)
				list_return.append(dictret)

			#print(list_return)
			result = json.dumps(list_return)
			#print(result)

			session.close()
			return result, 200
		else:
			session.close()
			return jsonify({'Message': "Empty cart"}), 404
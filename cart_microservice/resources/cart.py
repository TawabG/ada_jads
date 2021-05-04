import json
import simplejson as json
from daos.cart_dao import CartDAO
from db import Session
from flask import jsonify


class Cart:
	@staticmethod
	def create(body):
		session = Session()
		cart = CartDAO(
			body['user_id'],
			body['product_id'],
			body['product_name'],
			body['product_quantity'],
			body['product_price'],
			'static short description',
			'/product/path',
			'path/to/img'
		)
 
		session.add(cart)
		session.commit()
		session.refresh(cart)
		session.close()
		#return jsonify({'Product added to cart!': "Product added to cart!"}), 200
		return jsonify({'Succes!': f'Product with name: {cart.product_name} has been added to the cart.'}), 200

	@staticmethod
	def get(user_id):
		session = Session()
		# compare cart_user_id in database with cart_user_id of json body
		cart = session.query(CartDAO).filter(CartDAO.user_id == user_id).all()

		# check if cart_user_id exists (thus if an item is in the cart)
		if cart:
			# if so, return all items in cart
			list_return = []
			for item in session.query(CartDAO).filter(CartDAO.user_id == user_id).all():
				dictret = dict(item.__dict__)
				dictret.pop('_sa_instance_state', None)
				list_return.append(dictret)

			result = json.dumps(list_return[0])

			session.close()
			return result, 200
		else:
			session.close()
			return jsonify({'Message': "Empty cart"}), 404

	# return jsonify({'test1': f'user_id: {user_id}'}), 200

	@staticmethod
	def update(user_id, req_data):
		session = Session()
		cart = session.query(CartDAO).filter(CartDAO.user_id == user_id).first()
		if cart:
			product_exist = session.query(CartDAO).filter(CartDAO.product_id == req_data['product_id']).first()
			# check if product exists
			if product_exist:
				product_exist.product_quantity = req_data['product_quantity']
				session.commit()
				return jsonify({'message': 'The cart product quantity is updated'}), 200
			else:
				session.close()
				return jsonify({'message': 'This product is not in the cart!'}), 404
		else:
			session.close()
			return jsonify({'message': 'You cannot update an non-existing cart!'}), 404

	@staticmethod
	def delete(user_id):
		session = Session()
		effected_rows = session.query(CartDAO).filter(CartDAO.user_id == user_id).delete()
		session.commit()
		session.close()
		if effected_rows == 0:
			return jsonify({'message': f'There is no cart with a cart id {user_id}'}), 404
		else:
			return jsonify({'message': 'The cart is removed'}), 200

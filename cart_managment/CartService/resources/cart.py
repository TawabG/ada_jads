from datetime import datetime

from flask import jsonify

from cartdaos.cart_dao import CartDAO
from db import Session


# create a cart and add and delete the cart
class Cart:
    @staticmethod
    def create(body):
        session = Session()
        cart = CartDAO(body['customer_id'],
                       body['product_id'],
                       body['product_name'],
                       body['product_quantity'],
                       datetime.now())
        session.add(cart)
        session.commit()
        session.refresh(cart)
        session.close()
        return jsonify({'cart_id': cart.id}), 200

    @staticmethod
    def get(c_id):
        session = Session()
        cart = session.query(CartDAO).filter(CartDAO.id == c_id).first()

        if cart:
            text_out = {
                "customer_id:": cart.customer_id,
                "product_id:": cart.product_id,
                "product_name": cart.product_name,
                "product_quantity": cart.product_quantity,
                "cart_added_time": cart.added_time.isoformat()
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no cart with a cart id {c_id}'}), 404

    def update(c_id, quantity):
        session = Session()
        cart = session.query(CartDAO).filter(CartDAO.id == c_id).first()
        cart.product_quantity = quantity
        session.commit()
        return jsonify({'message': 'The cart product quantity is updated'}), 200

    @staticmethod
    def delete(c_id):
        session = Session()
        effected_rows = session.query(CartDAO).filter(CartDAO.id == c_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no cart with a cart id {c_id}'}), 404
        else:
            return jsonify({'message': 'The cart is removed'}), 200
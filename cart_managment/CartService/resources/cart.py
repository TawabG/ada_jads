from datetime import datetime

from flask import jsonify

from constant import STATUS_CREATED
from cartdaos.cart_dao import CartDAO
from cartdaos.status_dao import StatusDAO
from db import Session


# shows an item in a cart and let to add or delete item
class Cart:
    @staticmethod
    def create(body):
        session = Session()
        cart = CartDAO(body['customer_id'], body['product_id'], datetime.now(),
                       StatusDAO(STATUS_CREATED, datetime.now()))
        session.add(cart)
        session.commit()
        session.refresh(cart)
        session.close()
        return jsonify({'cart_id': cart.id}), 200

    @staticmethod
    def get(c_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        cart = session.query(CartDAO).filter(CartDAO.id == c_id).first()

        if cart:
            status_obj = cart.status
            text_out = {
                "customer_id:": cart.customer_id,
                "product_id:": cart.product_id,
                "added_time": cart.added_time.isoformat(),
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no cart with id {c_id}'}), 404

    @staticmethod
    def delete(c_id):
        session = Session()
        effected_rows = session.query(CartDAO).filter(CartDAO.id == c_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no cart number with id {c_id}'}), 404
        else:
            return jsonify({'message': 'The cart is removed'}), 200


 #   def post(name):
 #       product_created = request.get_json(force=True)
 #       name = product_created["name"]
 #       quantity = product_created["quantity"]
 #       for product in CART:
 #           if name == product["name"]:
 #               product["quantity"]=quantity
 #
 #           return product, 201
from flask import jsonify

from cartdaos.cart_dao import CartDAO
from db import Session

# shows an item in a cart and let to add or delete item

class CartList:

    def add_product(p_id, a_name):
        session = Session()
        cart = session.query(CartDAO).filter(CartDAO.product_id == p_id).first()
        cart.product_name = a_name
        cart.product_quantity += 1
        session.commit()
        return jsonify({'message': 'The cart product quantity is updated'}), 200

    def delete_product(p_id):
        session = Session()
        effected_rows = session.query(CartDAO).filter(CartDAO.product_id == p_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return

#   def post(name):
 #       product_created = request.get_json(force=True)
 #       name = product_created["name"]
 #       quantity = product_created["quantity"]
 #       for product in CART:
 #           if name == product["name"]:
 #               product["quantity"]=quantity
 #
 #           return product, 201
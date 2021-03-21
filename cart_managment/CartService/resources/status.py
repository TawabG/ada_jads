import datetime
from flask import jsonify
from cartdaos.cart_dao import CartDAO
from db import Session


class Status:
    @staticmethod
    def update(c_id, status):
        session = Session()
        cart = session.query(CartDAO).filter(CartDAO.id == c_id)[0]
        cart.status.status = status
        cart.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The cart status was updated'}), 200

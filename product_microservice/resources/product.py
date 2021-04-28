import os
from google.cloud import storage

from flask import jsonify

from productdaos.product_dao import ProductDAO
from db import Session
from datetime import datetime

class Product:
    @staticmethod
    def create(body):
        session = Session()
        product = ProductDAO(body['id'],
                             body['product_name'],
                             body['product_quantity'],
                             body['unit_price'],
                             datetime.now())
        session.add(product)
        session.commit()
        session.refresh(product)
        session.close()
        return jsonify({'product_id': product.id}), 200

    @staticmethod
    def get(p_id):
        session = Session()
        product = session.query(ProductDAO).filter(ProductDAO.id == p_id).first()

        if product:
            text_out = {
                "product_id: ": product.id,
                "product_name: ": product.product_name,
                "product_quantity: ": product.product_quantity,
                "unit_price: ": product.unit_price,
                "product_registered_time: ": product.added_time.isoformat()
            }
            session.clsoe()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'Could not get a product with id {p_id}'}), 404

    @staticmethod
    def update(p_id, quantity, unit_price):
        session = Session()
        product = session.query(ProductDAO).filter(ProductDAO.id == p_id).first()
        product.product_quantity = quantity
        product.unit_price = unit_price
        session.commit()
        return jsonify({'message': 'The product inventory quantity and/or unit price is updated'}), 200

    @staticmethod
    def delete(p_id):
        session = Session()
        delete_row = session.query(ProductDAO).filter(ProductDAO.id == p_id).delete()
        session.commit()
        session.close()
        if delete_row == 0:
            return jsonify({'message': f'There is no product to delete with id {p_id}'}), 404
        else:
            return jsonify({'message': 'The product is removed from db'}), 200
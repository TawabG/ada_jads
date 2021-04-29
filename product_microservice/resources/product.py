#%%
from datetime import datetime
from flask import jsonify
from db import Session
from daos.product_dao import ProductDAO
from sqlalchemy.sql import text

class Product:

    @staticmethod
    def create(body):
        session = Session()
        product = ProductDAO(body['id'],
                             body['title'],
                             body['overview'],
                             body['release_date'],
                             body['runtime'],
                             body['adult'],
                             body['original_language'],
                             body['budget'],
                             body['revenue'],
                             body['product_quantity'],
                             body['unit_price']
                             )
        session.add(product)
        session.commit()
        session.refresh(product)
        session.close()
        return jsonify({'product_id': product.id}), 200

    @staticmethod
    def get_recommendation_data():
        # TODO Implement failure if database is empty or does not exist
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm

        recommender_data = session.execute('SELECT title, overview FROM products')
        data_list = []
        for title, review in recommender_data:
            data_dict = {'title': title, 'review': review}
            print(review)
            data_list.append(data_dict)
        session.close()
        return jsonify(data_list), 200

    @staticmethod
    def get(p_id):
        session = Session()
        product = session.query(ProductDAO).filter(ProductDAO.id == p_id).first()

        if product:
            text_out = {
                "product_id: ": product.id,
                "product_name: ": product.title,
                "product_quantity: ": product.product_quantity,
                "unit_price: ": product.unit_price
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





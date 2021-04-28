#%%
from datetime import datetime
from flask import jsonify
from db import Session
from daos.product_dao import ProductDAO
from sqlalchemy.sql import text

class Product:
    @staticmethod
    def get():
        #TODO Implement failure if database is empty or does not exist
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




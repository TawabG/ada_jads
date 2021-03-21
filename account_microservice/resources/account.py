from datetime import datetime
from flask import jsonify
#from constant import STATUS_CREATED
from daos.account_dao import AccountDAO
from db import Session

class Account:

    @staticmethod
    def create_account(body):
        session = Session()
        account = AccountDAO(body['customer_name'],
                             body['customer_address'],
                             body['customer_email'],
                             body['customer_password'],
                             datetime.now())
        #Simply add objects to table, advantage of ORM
        session.add(account)
        session.commit()
        session.refresh(account)
        session.close()
        #Use Jsonify to return json object with status code when API is called.
        return jsonify({'customer_id': account.id}), 200

    def get_recommendation:
        session = Session()


    @staticmethod
    def get_account(a_email):
        session = Session()
        account = session.query(AccountDAO).filter(AccountDAO.customer_email == a_email).first()
        if account:
            text_out = {
                "customer_id": account.id,
                "customer_name": account.customer_name,
                "customer_address": account.customer_address,
                "customer_email": account.customer_email,
                #TODO maybe not return password if we get account haha.
                "customer_password": account.customer_password,
                "creation_time": account.creation_time
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message':f'There is no account with e-mail {a_email}'}), 404


    @staticmethod
    #TODO Extend this so other attributes can be updated too
    def update_account_name(a_id, a_name):
        session = Session()
        account = session.query(AccountDAO).filter(AccountDAO.id == a_id).first()
        account.customer_name = a_name
        session.commit()
        return jsonify({'message': 'The account name was updated'}), 200


    @staticmethod
    def delete_account(a_id):
        session = Session()
        effected_row = session.query(AccountDAO).filter(AccountDAO.id == a_id).delete()
        session.commit()
        session.close()
        if effected_row == 0:
            return jsonify({'message': f'There is no account with id {a_id}'}), 404
        else:
            return jsonify({'message': 'The account was removed'}), 200
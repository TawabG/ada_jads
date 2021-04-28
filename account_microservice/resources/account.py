from datetime import datetime
from flask import jsonify
# from constant import STATUS_CREATED
from daos.account_dao import AccountDAO
from db import Session
from datetime import datetime

# from constant import STATUS_CREATED
from daos.account_dao import AccountDAO
from db import Session
from flask import jsonify


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

    @staticmethod
    def get_account(body):
        session = Session()
        account_email = body['customer_email']
        account = session.query(AccountDAO).filter(AccountDAO.customer_email == account_email).first()
        if account:
            text_out = {
                "customer_id": account.id,
                "customer_name": account.customer_name,
                "customer_address": account.customer_address,
                "customer_email": account.customer_email,
                "creation_time": account.creation_time
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no account with e-mail {account_email}'}), 404

    @staticmethod
    def update_account_name(a_id, body):
        session = Session()
        account = session.query(AccountDAO).filter(AccountDAO.id == a_id).first()
        if account:
            entities_updated = []
            if 'customer_name' in body:
                account.customer_name = body['customer_name']
                entities_updated.append('customer_name, ')
            if 'customer_address' in body:
                account.customer_address = body['customer_address']
                entities_updated.append('customer_address, ')
            if 'customer_password' in body:
                account.customer_password = body['customer_password']
                entities_updated.append('customer_password, ')
            if 'customer_email' in body:
                account.customer_email = body['customer_email']
                entities_updated.append('customer_email, ')
            session.commit()
            session.close()
            return jsonify({'message': f'{" ".join(entities_updated)} were updated'}), 200
        else:
            session.close()
            return jsonify({'message': f'There is no account with id {a_id}'}), 404


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
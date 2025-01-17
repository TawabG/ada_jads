from flask import Flask, request

from db import Base, engine
from resources.account import Account

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/accounts/create_account', methods=['POST'])
def create_account():
    req_data = request.get_json()
    return Account.create_account(req_data)


@app.route('/accounts/get_account', methods=['GET'])
def get_account():
    #body = request.get_json()
    customer_email = request.args.get('customer_email')
    return Account.get_account(customer_email)


@app.route('/accounts/update_account', methods=['PUT'])
def update_account():
    cust_id = request.args.get('customer_id')
    body = request.get_json()
    return Account.update_account(cust_id, body)


@app.route('/accounts/delete_account', methods=['DELETE'])
def delete_account():
    customer_id = request.args.get('customer_id')
    return Account.delete_account(customer_id)

app.run(host='0.0.0.0', port=5000)
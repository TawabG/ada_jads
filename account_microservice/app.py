from flask import Flask, request
from db import Base, engine
from resources.account import Account

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/accounts', methods=['POST'])
def create_account():
    req_data = request.get_json()
    return Account.create_account(req_data)


@app.route('/accounts/<a_email>', methods=['GET'])
def get_account(a_email):
    return Account.get_account(a_email)


@app.route('/accounts/<a_id>', methods=['PUT'])
def update_account_name(a_id):
    account_name = request.args.get('account_name')
    return Account.update_account_name(a_id, account_name)


@app.route('/accounts/<a_id>', methods=['DELETE'])
def delete_account(a_id):
    return Account.delete_account(a_id)


app.run(host='0.0.0.0', port=5000)
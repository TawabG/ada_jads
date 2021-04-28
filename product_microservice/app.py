from flask import Flask, request
from db import Base, engine
from resources.product import Product

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/products/get_data', methods=['GET'])
def get_data():
    return Product.get()

app.run(host='0.0.0.0', port=5000)

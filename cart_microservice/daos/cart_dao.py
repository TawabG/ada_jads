from db import Base
from sqlalchemy import Column, String, Integer, Numeric, Float, Boolean


class CartDAO(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product_id = Column(String)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Numeric)
    product_short_description = Column(String)
    product_url = Column(String)
    product_image_url = Column(String)

    def __init__(self, user_id, product_id, product_name, product_quantity, product_price, product_short_description,
                 product_url, product_image_url):
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_short_description = product_short_description
        self.product_url = product_url
        self.product_image_url = product_image_url

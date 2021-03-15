from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship, backref

#from daos.status_dao import StatusDAO
from db import Base


class CartDAO(Base):
    __tablename__ = 'cart2'
    id = Column(Integer, primary_key=True)
    cart_user_id = Column(Integer)
    product_id = Column(String)
    product_name  = Column(String)
    product_price = Column(Numeric)
    product_short_description = Column(String)
    product_url = Column(String)
    product_image_url  = Column(String)
    amount = Column(Integer)


    def __init__(self, cart_user_id, product_id, product_name, product_price, product_short_description, product_url, product_image_url, amount):
        self.cart_user_id = cart_user_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_short_description = product_short_description
        self.product_url = product_url
        self.product_image_url = product_image_url
        self.amount = amount
        
from db import Base
from sqlalchemy import Column, String, Integer, Float, Boolean


class ProductDAO(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    adult = Column(Boolean)
    budget = Column(Integer)
    original_language = Column(String)
    overview = Column(String)  # Essential for recommender
    release_date = Column(String)
    revenue = Column(Float)
    runtime = Column(Integer)
    title = Column(String)  # Essential for recommender

    # product_quantity = Column(String)
    # unit_price = Column(Numeric)

    def __init__(self, adult, budget, original_language, overview, release_date, revenue, runtime, title,
                 product_quantity, unit_price):
        self.adult = adult
        self.budget = budget
        self.original_language = original_language
        self.overview = overview
        self.release_date = release_date
        self.revenue = revenue
        self.runtime = runtime
        self.title = title
        # self.product_quantity = product_quantity
        # self.unit_price = unit_price

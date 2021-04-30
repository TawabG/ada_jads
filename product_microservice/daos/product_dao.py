from db import Base
from sqlalchemy import Column, String, Integer, Float, Boolean

class ProductDAO(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String)  # Essential for recommender
    overview = Column(String)  # Essential for recommender
    release_date = Column(String)
    runtime = Column(Integer)
    adult = Column(Boolean)
    original_language = Column(String)
    budget = Column(Integer)
    revenue = Column(Float)
    product_quantity = Column(Integer)
    unit_price = Column(Float)

    def __init__(self, title, overview, release_date, runtime, adult, original_language,
                 budget, revenue, product_quantity, unit_price):
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.runtime = runtime
        self.adult = adult
        self.original_language = original_language
        self.budget = budget
        self.revenue = revenue
        self.product_quantity = product_quantity
        self.unit_price = unit_price
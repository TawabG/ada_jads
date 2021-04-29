<<<<<<< Updated upstream
=======
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Boolean
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    overview = Column(String)  # Essential for recommender
    release_date = Column(String)
    revenue = Column(Float)
    runtime = Column(Integer)
    title = Column(String)  # Essential for recommender

    # product_quantity = Column(String)
    # unit_price = Column(Numeric)

    def __init__(self, adult, budget, original_language, overview, release_date, revenue, runtime, title):
        # product_quantity, unit_price
        self.adult = adult
        self.budget = budget
        self.original_language = original_language
=======
    budget = Column(Integer)
    revenue = Column(Float)
    product_quantity = Column(Integer)
    unit_price = Column(String)

    def __init__(self, title, overview, release_date, runtime, adult, original_language,
                 budget, revenue, product_quantity, unit_price):
        self.title = title
>>>>>>> Stashed changes
        self.overview = overview
        self.release_date = release_date
        self.runtime = runtime
<<<<<<< Updated upstream
        self.title = title
        # self.product_quantity = product_quantity
        # self.unit_price = unit_price
=======
        self.adult = adult
        self.original_language = original_language
        self.budget = budget
        self.revenue = revenue
        self.product_quantity = product_quantity
        self.unit_price = unit_price
>>>>>>> Stashed changes

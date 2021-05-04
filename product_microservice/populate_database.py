# %%
import random

import pandas as pd

from daos.product_dao import ProductDAO
from db import Session


def populate_db():
    df = pd.read_csv('data/movies_metadata.csv')

    # TODO make sure release_date is right type
    df_sub = df[
        ['adult', 'budget', 'original_language', 'overview', 'release_date', 'revenue', 'runtime', 'title']].copy()

    # os.environ['DB_URL'] = 'sqlite:///delivery.db'
    # 2 - generate database schema
    # Base.metadata.create_all(engine)

    # 3 - create a new session
    session = Session()

    # How to connect to existing database.
    for index, row in df_sub.iterrows():
        adult = row['adult']
        budget = row['budget']
        orlang = row['original_language']
        overview = row['overview']
        reldate = row['release_date']
        revenue = row['revenue']
        runtime = row['runtime']
        title = row['title']
        product_quantity = random.randint(1000, 5000)
        unit_price = random.randint(100, 500) / 100
        population_objects = ProductDAO(adult=adult, budget=budget, original_language=orlang,
                                        overview=overview, release_date=reldate, revenue=revenue,
                                        runtime=runtime, title=title,
                                        product_quantity=product_quantity, unit_price=unit_price)
        session.add(population_objects)
        session.commit()
        session.refresh(population_objects)
        session.close()
    print("Db Successfully populated")

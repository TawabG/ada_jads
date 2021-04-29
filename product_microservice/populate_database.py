# %%
import pandas as pd

from daos.product_dao import ProductDAO
from db import Session, engine, Base

df = pd.read_csv('../recommender_microservice/data/movies_metadata.csv')

# TODO make sure release_date is right type
df_sub = df[['adult', 'budget', 'original_language', 'overview', 'release_date', 'revenue', 'runtime', 'title']].copy()

# os.environ['DB_URL'] = 'sqlite:///delivery.db'
# 2 - generate database schema
Base.metadata.create_all(engine)
# 3 - create a new session
session = Session()

for index, row in df_sub.iterrows():
    adult = row['adult']
    budget = row['budget']
    orlang = row['original_language']
    overview = row['overview']
    reldate = row['release_date']
    revenue = row['revenue']
    runtime = row['runtime']
    title = row['title']
    population_objects = ProductDAO(adult=adult, budget=budget, original_language=orlang, overview=overview, release_date=reldate, revenue=revenue, runtime=runtime, title=title)
    session.add(population_objects)
    # # 10 - commit and close session



session.commit()
session.close()



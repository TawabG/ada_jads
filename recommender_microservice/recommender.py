#%%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#%%Resize df
metadata = pd.read_csv('../product_microservice/data/movies_metadata_full.csv')
meta_data_sub = metadata[:201]
meta_data_sub.to_csv('data/movies_metadata.csv')
metadata_sub_reload = pd.read_csv('../product_microservice/data/movies_metadata.csv')

#%%
tfidf = TfidfVectorizer(stop_words='english')
#Why would we fit it on movie descriptions? Shouldn't we fit it on other attributes
metadata['overview'] = metadata['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(metadata['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()


# %%
def get_recommendations(title, cosine_sim_param):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim_param[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return metadata['title'].iloc[movie_indices]


get_recommendations('The Dark Knight Rises', cosine_sim)
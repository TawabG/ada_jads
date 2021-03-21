import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class SimpleRecommender:

    @staticmethod
    def recommend(movie_name):
        movie_df = pd.read_csv('data/movies_metadata.csv', error_bad_lines=False)
        tfidf = TfidfVectorizer(stop_words='english')
        movie_df['overview'].fillna('', inplace=True)
        tfidf_matrix = tfidf.fit_transform(movie_df['overview'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(movie_df.index, index=movie_df['title']).drop_duplicates()
        idx = indices[movie_name]

        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]

        return movie_df['title'].iloc[movie_indices].to_json(), 200

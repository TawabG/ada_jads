import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from daos.recommender_dao import recommenderDAO
from db import Session

class Recommender:
    @staticmethod
    def get(m_id):
        session = Session()

        recommendation = session.query(recommenderDAO).filter(recommenderDAO.id == m_id).first()

        if recommendation:
            text_out = {
                "title:": recommender.title
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no recommendation for this movie'}), 404



class SimpleRecommender:

    def __init__(self):
        self.model = None

    def recommend(self, request):
        metadata = pd.read_csv('movies_metadata.csv', low_memory=True)

        tfidf = TfidfVectorizer(stop_words='english')

        metadata['overview'] = metadata['overview'].fillna('')

        tfidf_matrix = tfidf.fit_transform(metadata['overview'])

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

        def get_recommendations(title, cosine_sim=cosine_sim):
            idx = indices[title]

            sim_scores = list(enumerate(cosine_sim[idx]))

            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            sim_scores = sim_scores[1:11]

            movie_indices = [i[0] for i in sim_scores]

            return metadata['title'].iloc[movie_indices]
        
        get_recommendations('the dark knight')

        print(get_recommendations(request))
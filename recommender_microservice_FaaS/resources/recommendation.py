import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class SimpleRecommender:

    def recommend(movie_name, movie_titles, movie_overviews):
        # Make connection with google cloud bucket
        # project_id = 'adv-data-architectures'
        # bucket_name = 'ada-assignment'
        # file_name = 'movies_metadata.csv'
        # client = storage.Client(project=project_id)
        # bucket = client.get_bucket(bucket_name)
        # blob = bucket.blob(file_name)
        # temp_filename = os.path.join('/tmp', file_name)
        # blob.download_to_filename(temp_filename)
        # # use temp_filename (which should be movies_metadata.csv)
        # movie_df = pd.read_csv(temp_filename, error_bad_lines=False)
        # movie_df = pd.read_csv('data/movies_metadata.csv', error_bad_lines=False)

        titles = movie_titles
        overviews = movie_overviews
        movie_df = pd.DataFrame(columns=['titles', 'overviews'])
        movie_df['titles'] = titles
        movie_df['overviews'] = overviews

        tfidf = TfidfVectorizer(stop_words='english')
        movie_df['overviews'].fillna('', inplace=True)
        tfidf_matrix = tfidf.fit_transform(movie_df['overviews'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        indices = pd.Series(movie_df.index, index=movie_df['titles']).drop_duplicates()
        idx = indices[movie_name]

        sim_scores = list(enumerate(cosine_sim[idx]))
        #sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]

        return movie_df['titles'].iloc[movie_indices].to_json(), 200

        # Allocate 1GiB in Google Cloud functions!!


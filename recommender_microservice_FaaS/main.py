from resources.recommendation import SimpleRecommender

def get_recommendation(request):

    print(request.path)
    
    from flask import abort, jsonify

    if request.method == 'POST':
        # Alternative method
        # request_args = request.args
        # movie_name = request_args['movie_name']


        return jsonify({'testing': 'recommender'}), 200

        # request_movie = request.args.get('movie_name')
        # request_overviews = request.args.get('overviews')
        # request_titles = request.args.get('title')

        # return SimpleRecommender.recommend(movie_name=request_movie,
        #                                    movie_overviews=request_overviews,
        #                                    movie_titles=request_titles)

    else:
        return abort(404)


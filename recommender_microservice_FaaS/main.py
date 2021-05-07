from resources.recommendation import SimpleRecommender

def get_recommendation(request):

    print(request.path)

    from flask import abort

    if request.method == 'POST':
        req_data = request.get_json()
        print(req_data)
        request_movie = req_data['movie_name']
        request_overviews = req_data['overviews']
        request_titles = req_data['titles']
        #return jsonify({"Succes!": f"Movie: {request_movie} testing"}), 200


        # return SimpleRecommender.recommend(movie_name=request_movie,
        #                                    movie_overviews=request_overviews,
        #                                    movie_titles=request_titles)

        # request_movie = request.args.get('movie_name')
        # request_overviews = request.args.get('overviews')
        # request_titles = request.args.get('title')

        return SimpleRecommender.recommend(movie_name=request_movie,
                                           movie_overviews=request_overviews,
                                           movie_titles=request_titles)

    else:
        return abort(404)


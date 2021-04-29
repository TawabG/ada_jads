from resources.recommendation import SimpleRecommender

def get_recommendation(request):
    print(request.path)
    from flask import abort
    if request.method == 'GET':
        # Alternative method
        #request_args = request.args
        #movie_name = request_args['movie_name']

        request_arg = request.args.get('movie_name')
        return SimpleRecommender.recommend(movie_name=request_arg)

    else:
        return abort(405)


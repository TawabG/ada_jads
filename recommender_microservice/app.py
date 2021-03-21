from flask import Flask, request
from resources.first_recommender import SimpleRecommender


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/recommendations/', methods=['GET'])
def recommend():
    request_arg = request.args.get('movie_name')
    return SimpleRecommender.recommend(movie_name=request_arg)

sr = SimpleRecommender()
app.run(host='0.0.0.0', port=5000)

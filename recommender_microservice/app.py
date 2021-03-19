from flask import Flask, request

from resources.first_recommender import SimpleRecommender

app = Flask(__name__)
app.config["DEBUG"] = True

model = None

@app.route('/recommendations/<r_id>', methods=['GET'])
def recommend():
    return sr.recommend(request)


sr = SimpleRecommender()
app.run(host='0.0.0.0', port=5000)

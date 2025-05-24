#DISINI KITA AKAN MENCOBA MENJADI BACK END ENGINEER
from flask import Flask, request, jsonify
from utils.predictor import predict_stunting, predict_wasting
from utils.recommender import recommend_articles

app = Flask(__name__)

@app.route('/predict_stunting', methods=['POST'])
def stunting_route():
    data = request.json
    input_features = data['features']
    label = predict_stunting(input_features)
    articles = recommend_articles(label)
    return jsonify({'prediction': label, 'articles': articles})

@app.route('/predict_wasting', methods=['POST'])
def wasting_route():
    data = request.json
    input_features = data['features']
    label = predict_wasting(input_features)
    articles = recommend_articles(label)
    return jsonify({'prediction': label, 'articles': articles})

if __name__ == '__main__':
    app.run(debug=True)

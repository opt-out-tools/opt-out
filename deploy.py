import os
import urllib.parse
from flask import Flask, request, jsonify
from keras import backend, models
from models.neural_net.simple_dataturks import Model

app = Flask(__name__)

m = Model()

@app.route("/predict")
def generate_sentiment_score():
    """Returns the sentiment score of the parsed sentence.

    Returns:
        score (int) : The sentiment score of the sentence. 1 - abusive, 0 - not abusive.
    """

    sentence = request.args.get("sentence")

    backend.clear_session()

    score = m.predict(urllib.parse.unquote(sentence), os.getcwd() + "/models/neural_net/simple_dataturks.h5",
              "/models/neural_net/simple_dataturks_dict.csv", 'content', 10000)
    return jsonify(score=score)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

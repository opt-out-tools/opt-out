import os
import urllib.parse
from flask import Flask
from flask import request
from flask import jsonify
from keras import backend
from src.optout.model import Model

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

    score = m.predict(urllib.parse.unquote(sentence), os.getcwd() + "/saved_data/models/model_120.h5",
              "/data/DataTurks/dump.csv", 'content', 10000)
    return jsonify(score=score)


if __name__ == "__main__":
    app.run()

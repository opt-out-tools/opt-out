import os
import urllib.parse

import pandas as pd
from flask import Flask
from flask import request
from keras.models import load_model

from model import predict, create_dictionary

app = Flask(__name__)

data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
corpus_vocabulary = create_dictionary(data['content'], 10000)

model = load_model(os.getcwd() + "/saved_model_data/models/model_120.h5")
model._make_predict_function()


@app.route("/test")
def generate_sentiment_score():
    """Returns the sentiment score of the parsed sentence.

    Returns:
        score (int) : The sentiment score of the sentence. 1 - abusive, 0 - not abusive.
    """

    sentence = request.args.get("sentence")
    score = predict(urllib.parse.unquote(sentence), model, corpus_vocabulary)[0]

    if score >= 0.5:
        return "That's not very nice."
    else:
        return "Ooo aren't you sweet."


if __name__ == "__main__":
    app.run()

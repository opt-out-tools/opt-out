import os
import urllib.parse

import pandas as pd
from flask import Flask
from flask import request
from keras.models import load_model

from model import test, create_dictionary

app = Flask(__name__)


@app.route("/test")
def generate_sentiment_score():
    """Returns the sentiment score of the parsed sentence.

    Returns:
        score (int) : The sentiment score of the sentence. 1 - abusive, 0 - not abusive.
    """
    train_data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
    corpus_vocabulary = create_dictionary(train_data['content'])

    model = load_model("stored_models/model_120.h5")
    model._make_predict_function()

    sentence = request.args.get("sentence")
    return str(test(urllib.parse.unquote(sentence), model, corpus_vocabulary))


if __name__ == "__main__":
    app.run()

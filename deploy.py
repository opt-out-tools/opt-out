import urllib.parse

from flask import Flask
from flask import request
from keras.models import load_model
import os
import pandas as pd

from model import train, test, create_dictionary

app = Flask(__name__)


train_data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
corpus_vocabulary = create_dictionary(train_data['content'])


model = load_model("model_120.h5")
model._make_predict_function()


@app.route("/test")
def generate_sentiment_score():
    """Returns the sentiment score of the parsed sentence.
    Args:
        query parameter : The sentence to analyse
    Return:
        score (int) : The sentiment score of the sentence. 1 - abusive, 0 - not abusive.
    """
    sentence = request.args.get("sentence")
    return test(urllib.parse.unquote(sentence), model, corpus_vocabulary)


if __name__ == "__main__":
    app.run()

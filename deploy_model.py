import urllib.parse

from flask import Flask
from flask import request
from keras.models import load_model

from model import train, test

app = Flask(__name__)

m, tokenizer = train()
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
    return test(urllib.parse.unquote(sentence), model, tokenizer)


if __name__ == "__main__":
    app.run()

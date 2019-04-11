from flask import Flask
from model import execute
from flask import request
import urllib.parse

app = Flask(__name__)


@app.route("/sentence")
def run_model():
    sentence = request.args.get("sentence")
    return execute(urllib.parse.unquote(sentence))


if __name__ == "__main__":
    app.run()
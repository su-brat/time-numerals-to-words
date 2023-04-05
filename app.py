from flask import Flask, request
from services.time_to_words import get_in_words

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! To get the time in words, go to '/numeral-to-word'.</p>"


@app.route("/numeral-to-word")
def fetch_word():
    args = request.args
    try:
        h = int(args.get('h'))
        m = int(args.get('m'))
        response = get_in_words(h, m)
        if response:
            return response, 200
        raise Exception()
    except:
        return "Please pass valid 'h' and 'm' values as query parameters.", 400

app.run()

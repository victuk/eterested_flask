from flask import Flask
from extractor import extract_topics

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/text")
def ext():
    data = request.get_json()
    return extract_topics(data.topic)
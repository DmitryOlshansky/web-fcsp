#!/usr/bin/env python
# coding=UTF-8
from flask import Flask, request, Response, render_template
from encoder import encode_mols

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/encode_one", methods=["POST"])
def encode_one():
    f = request.files['file']
    data = f.read()
    codes = encode_mols.delay([data]).get()
    print codes
    return "\n".join(codes)

@app.route("/encode_many", methods=["POST"])
def encode_many():
    files = request.files
    print files
    """data = map(lambda f : f.read(), files)
    chunks = [data[i:i + n] for i in range(0, len(data), 10)]
    futures = map(lambda chunk: encode_mols.delay(chunk), chunks)
    responses = map(lambda f: f.get(), futures)
    result = {}
    for r in responses:
        result[]
    return data"""
    return "OK"


if __name__ == '__main__':
    import sys
    reload(sys)    
    sys.setdefaultencoding("utf-8")
    app.run(debug=True)

#!/usr/bin/env python
# coding=UTF-8
from flask import Flask, request, Response, render_template
from encoder import encode_mols
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/encode_one", methods=["POST"])
def encode_one():
    f = request.files['file']
    data = f.read()
    codes = encode_mols.delay([data]).get()
    ret = json.loads("\n".join(codes))[0]
    return Response(json.dumps(ret), mimetype="application/json")

@app.route("/encode_many", methods=["POST"])
def encode_many():
    files = request.files
    names = files.keys()
    data = map(lambda f : f.read(), files.values())
    n = 10
    chunks = [data[i:i + n] for i in range(0, len(data), n)]
    futures = map(lambda chunk: encode_mols.delay(chunk), chunks)
    responses = map(lambda f: f.get(), futures)
    result = {}
    flat = [item for batch in responses for item in batch]
    for i in range(len(flat)):
        result[names[i]] = json.loads(flat[i])[0]
    return Response(json.dumps(result), mimetype="application/json")

if __name__ == '__main__':
    import sys
    reload(sys)    
    sys.setdefaultencoding("utf-8")
    app.run(debug=True)

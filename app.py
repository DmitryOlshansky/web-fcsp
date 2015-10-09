#!/usr/bin/env python
# coding=UTF-8
from flask import Flask, request, Response, render_template
import subprocess
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/encode", methods=["POST"])
def projects_list():
    f = request.files['file']
    data = f.read()
    print data
    proc = subprocess.Popen("fcss-2a".split(),
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    data = proc.communicate(data)    
    return data

if __name__ == '__main__':
    import sys
    reload(sys)    
    sys.setdefaultencoding("utf-8")
    app.run(debug=True)

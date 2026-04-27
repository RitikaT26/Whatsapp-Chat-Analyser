from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import parsechat
from analyser import analyse
import os

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analysechat():
    f= request.files['file']
    fp= 'chat.txt'
    f.save(fp)

    df= parsechat(fp)
    res= analyse(df)
    os.remove(fp)
    return jsonify(res)
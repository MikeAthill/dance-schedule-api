from flask import Flask, request, jsonify
import pandas as pd
import pdfplumber
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Dance Competition Schedule API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
app = Flask(__name__)






@app.route('/')
def home1():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(debug=True)
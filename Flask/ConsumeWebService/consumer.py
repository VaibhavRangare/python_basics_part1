import requests
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/courses')
def index():
   session = requests.Session()
   session.trust_env = False
   ret = session.get('http://localhost:6700/home')
   return ret.json()

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0',port=6800)
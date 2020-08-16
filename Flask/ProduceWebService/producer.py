from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/home')
def index():
    x = {
    "name": "John",
    "age": 33,
    "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    return y

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0',port=6700)
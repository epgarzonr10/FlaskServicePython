from flask import Flask
app = Flask(__name__)

@app.route('/gethello')
def hello_world():
    return 'Good morning with everyone, my name is Edgar!'

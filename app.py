from flask import Flask
import consumer

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/messages')
def message():
    consumer.read_messages()
    return 'Reading messages view console'
from flask import Flask, request

from src import UserRepository

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, world!'


@app.route('/insert', methods=['POST'])
def insert():
    userRepository = UserRepository()
    body = request.json()
    userRepository.insert(body['name'])

    return 'OK'

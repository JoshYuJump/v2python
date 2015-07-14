import base64
import random
import time

from flask import Flask, request

app = Flask(__name__)

users = {
    "josh": ["123456"]
}

def get_token(uid):
    token = base64.b64encode(':'.join([
        str(uid),
        random.random(),
        time.time() + 7200
    ]))
    users[uid].append(token)
    return token

def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return 1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0

@app.route('/index', methods=['POST', 'GET'])
def index():
    print request.headers
    return 'Hello'

@app.route('/login', methods=['GET', 'POST'])
def login():
    print request.headers
    uid, pw = base64.b64decode(request.headers['Authorization'].split(':')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return get_token(uid)
    else:
        return 'error'

@app.route('/test', methods=['GET', 'POST'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'


if __name__ == '__main__':
    app.run(debug=True)
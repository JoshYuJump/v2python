
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
    

@app.route('/index')
def index():
    print request.headers
    return 'Hello'

@app.route('/login')
def login():
    pass

@app.route('/test')
def test():
    pass


if __name__ == '__main__':
    app.run(debug=True)
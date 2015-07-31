import base64
import random
import time

from flask import Flask, request, redirect

app = Flask(__name__)

auth_code = {}

# OAuth 2.0
@app.route('/client/login', methods=['GET', 'POST'])
def client_login():
    uri = 'http://localhost:5000/oauth'
    return redirect(uri)

@app.route('/oauth', methods=['GET', 'POST'])
def oauth():
    return 'please login'

def gen_code(uri):
    code = random.randint(0, 10000)
    auth_code[code] = uri
    return code

if __name__ == '__main__':
    app.run(debug=True)

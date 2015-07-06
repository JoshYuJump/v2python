
from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
def index():
    print request.headers
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
    return render_template('hello.jade')

if __name__ == '__main__':
    app.run(debug=True)
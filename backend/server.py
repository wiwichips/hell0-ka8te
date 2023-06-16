#!/usr/bin/env python3
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/hello')
def hello():
    return 'Hello, world!'

@app.route('/api/status')
def status():
    return '', 200

if __name__ == '__main__':
    app.run(port=8080)


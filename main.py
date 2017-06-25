# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Welcome'


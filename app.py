from flask import flask

app = flask(__name__)

@app.route('/')

def counter():
  return 'Hello World'

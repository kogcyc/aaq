import flask
import os

app = flask.Flask(__name__)

secret_string = os.getenv('SUPER_SECRET')

@app.route('/')
def index():
    return f'<span style="font-size: 2em; font-weight: 900;">{secret_string}</span>'

if __name__ == '__main__':
    app.run()

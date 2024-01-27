import flask
import os

app = flask.Flask(__name__)

secret_string = os.getenv('SUPER_SECRET')
secret_string = 'SUPER_SECRET'

@app.route('/')
def index():
    return f'<span style="padding: 40px; font-size: 2em; font-weight: 900; font-family: sans-serif; color: #fff; background-color: #9bd;">{secret_string}</span>'

if __name__ == '__main__':
    app.run()

import base64
from flask import Flask, request, jsonify, render_template
from github import Github
from github import Auth
import os

app = Flask(__name__)

ss = os.getenv('SUPER_SECRET')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_content = uploaded_file.read()
        auth = Auth.Token(ss)
        g = Github(auth=auth)
        repo_name = "kogcyc/imago"
        file_name = uploaded_file.filename 
        repo = g.get_repo(repo_name)
        repo.create_file(file_name, "commit message", bytes(file_content)) 
        return(file_name)

if __name__ == '__main__':
    app.run(debug=False)
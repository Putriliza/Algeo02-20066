import os
from flask import Flask, send_file
from api import api_blueprint

app = Flask(__name__, static_folder='../frontend/dist')
app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    dist_dir = '../frontend/dist'
    entrypoint = os.path.join(dist_dir, 'index.html')
    return send_file(entrypoint)

app.run(port=5000)
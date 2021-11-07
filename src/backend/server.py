from flask import Flask, render_template
from api import api_blueprint
from flask_cors import CORS

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist'
            )
app.register_blueprint(api_blueprint)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

app.run(port=5000)
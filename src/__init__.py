from flask import *
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
Bootstrap(app)

@app.route('/')
def main(): return render_template('index.html')
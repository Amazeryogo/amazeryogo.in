from flask import *
import json
import hashlib
import requests
from flask_bootstrap import Bootstrap
from src.links import *

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    # get gravatar image
    gravatar = "https://www.gravatar.com/avatar/%s?d=identicon&s=200" % hashlib.md5(
        email.encode()).hexdigest()
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    return render_template('index.html', ip=ip, gravatar=gravatar,books=favbooks)


@app.route('/contactme')
def contact():
    return render_template('contactme.html', email=email,instagram=instagram, reddit=reddit, twitch=twitch, youtube=youtube, spotify=spotify, thought=thought, blog=blog, github=github,favbooks=favbooks)

@app.route('/projects')
def projects():
    # get all repos from api.github.com
    repos = json.loads(requests.get("https://api.github.com/users/Amazeryogo/repos").text)
    return render_template('projects.html', repos=repos)

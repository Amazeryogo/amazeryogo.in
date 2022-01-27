from flask import *
import json
import hashlib
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # get gravatar image
    gravatar = "https://www.gravatar.com/avatar/%s?d=identicon&s=200" % hashlib.md5(
        "suvid.datta@gmail.com".encode()).hexdigest()
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return render_template('index.html', ip=ip, gravatar=gravatar)


@app.route('/contactme', methods=['GET', 'POST'])
def contact():
    email = "suvid.datta@gmail.com"
    github = "https://github.com/Amazeryogo"
    reddit = "https://www.reddit.com/user/Amazeryogo"
    twitch = "https://www.twitch.tv/amazeryogo29"
    youtube = "https://www.youtube.com/channel/UCTqxrChE3FXhy_yJg93pX4A"
    spotify = "https://open.spotify.com/user/p46kuy15wgr1aa8x132asq9o4?si=65c67f78ee5e4e81"
    return render_template('contactme.html', email=email, github=github, reddit=reddit, twitch=twitch, youtube=youtube,
                           spotify=spotify)


@app.route('/projects')
def projects():
    # get all repos from api.github.com
    repos = json.loads(requests.get("https://api.github.com/users/Amazeryogo/repos").text)
    return render_template('projects.html', repos=repos)

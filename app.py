import waitress
import src
import os

waitress.serve(src.app, host='127.0.0.1', port=5000)
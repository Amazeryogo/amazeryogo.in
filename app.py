import waitress
import src
import os

waitress.serve(src.app, host='0.0.0.0', port=os.getenv('PORT'))
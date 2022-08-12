from src import *
import waitress

waitress.serve(app, host='0.0.0.0', post=os.getenv('PORT'))
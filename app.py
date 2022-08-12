from src import *
import waitress

waitress.serve(app, host='0.0.0.0', port=os.getenv('PORT'))
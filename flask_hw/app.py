from flask import Flask, json
import logging


log_config = '%(asctime)s %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(format=log_config, level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'secret key'

from views import *



if __name__ == '__main__':
    app.run()

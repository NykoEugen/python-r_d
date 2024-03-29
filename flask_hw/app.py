from flask import Flask
import logging
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy

from config import AppConfig

# log_config = '%(asctime)s %(levelname)s in %(module)s: %(message)s'
# logging.basicConfig(format=log_config, level=logging.INFO)

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfig)
db.init_app(app)


from views import *
from models import *

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))

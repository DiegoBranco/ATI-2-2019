from flask import Flask, request, session
from flask_pymongo import PyMongo
from flask_babel import Babel
from flask_debug import Debug
# from flask.ext.session import Session
from .config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
# mongo = PyMongo(app, connect=False)
Debug(app)
babel = Babel(app)
mongo = MongoEngine(app)

# SESSION_TYPE = 'redis'
# sess = Session()
# sess.init_app(app)

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return "es"

if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0') 
    print("server running")

from app import routes
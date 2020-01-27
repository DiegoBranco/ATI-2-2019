from flask import Flask, request
from flask_pymongo import PyMongo
from flask_babel import Babel
from flask_debug import Debug


from config import Config


app = Flask(__name__)
app.config.from_object(Config)
    
mongo = PyMongo(app)
Debug(app)

babel = Babel(app)
@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return "es"



if __name__ == "__main__":
    app.run(debug=True)



from app import routes
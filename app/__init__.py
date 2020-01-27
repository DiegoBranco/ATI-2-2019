from flask import Flask
from config import Config
from flask_debug import Debug


app = Flask(__name__)
app.config.from_object(Config)

Debug(app)

if __name__ == "__main__":
    app.run(debug=True)

from app import routes
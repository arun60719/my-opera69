from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from ruotes import user_bp
from models import set_mongo

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb+srv://g7317088:<db_password>@cluster0.ixsn5wd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

mongo = PyMongo(app)
set_mongo(mongo)

app.register_blueprint(user_bp, url_prefix="/api")
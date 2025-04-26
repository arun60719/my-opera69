from flask import Flask
from models import set_mongo
from routes import user_bp

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://g7317088:ffffDDD5555@cluster0.ixsn5wd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

set_mongo(app)

app.register_blueprint(user_bp)

if __name__ == '_main_':
    app.run(host="0.0.0.0",port=5000)
from mongoengine import connect, Document, StringField

def set_mongo(app):
    connect(
        host=app.config["MONGO_URI"]
    )

class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
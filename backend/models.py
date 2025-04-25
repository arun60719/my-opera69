from bson.objectid import ObjectId

mongo = None

def set_mongo(m):
    global mongo
    mongo = m

class User:
    def _init_(self, email, password):  # Corrected init
        self.email = email
        self.password = password

    def save(self):
        user_data = {
            "email": self.email,
            "password": self.password,
            "mini_screens": []
        }
        result = mongo.db.users.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def get_mini_screens(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return user.get("mini_screens", []) if user else []

    @staticmethod
    def update_mini_screens(user_id, mini_screens):
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"mini_screens": mini_screens}}
)

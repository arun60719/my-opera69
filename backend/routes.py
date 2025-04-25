from flask import Blueprint, request, jsonify

from models import User  # Make sure models.py exists
user_bp = Blueprint('users', _name_)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(data["email"], data["password"])
    user_id = user.save()
    return jsonify({"message": "User registered", "user_id":user_id}) 

if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    if User.find_by_email(email):
        return jsonify({"message": "User with this email already exists"}), 409

    new_user = User(email=email, password=password)
    user_id = new_user.save()
    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.find_by_email(email)
    if user and user['password'] == password:
        return jsonify({"message": "Login successful", "user_id": str(user['_id'])}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@user_bp.route('/<user_id>/mini_screens', methods=['GET'])
def get_user_mini_screens(user_id):
    mini_screens = User.get_mini_screens(user_id)
    return jsonify(mini_screens), 200

@user_bp.route('/<user_id>/mini_screens', methods=['POST'])
def update_user_mini_screens(user_id):
    data = request.get_json()
    User.update_mini_screens(user_id, data)
    return jsonify({"message": "Mini-screen data updated successfully"}),200

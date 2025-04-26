from flask import Blueprint, request, jsonify
from models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    if User.objects(email=email):
        return jsonify({"error": "User already exists"}), 400
    
    user = User(email=email, password=password)
    user.save()
    return jsonify({"message": "User registered successfully"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.objects(email=email, password=password).first()
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}),200

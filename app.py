from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" (list of dicts)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob",   "email": "bob@example.com"}
]

@app.route('/', methods=['GET'])
def index():
    return "User Management API (Flask) - Use /users endpoints", 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET one user by id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# POST create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    # basic validation
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Both 'name' and 'email' are required"}), 400

    # auto-assign id (max id + 1)
    new_id = max((u['id'] for u in users), default=0) + 1
    new_user = {"id": new_id, "name": name, "email": email}
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    # Only update allowed fields
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']

    return jsonify(user), 200

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if not any(u['id'] == user_id for u in users):
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    # debug=True gives helpful error messages while developing
    app.run(host='127.0.0.1', port=5000, debug=True)

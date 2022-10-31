from flask import jsonify, request
from lb import app

USERS = [
    {
        "id": 1,
        "name": "Anna Zusova"
    },
    {
        "id": 2,
        "name": "Egor Forkov"
    }
]

@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['POST'])
def create_user():
    request_data = request.get_json()
    USERS.append(request_data)
    return jsonify({"status": "ok"})

@app.route("/user", methods=['PUT'])
def change_user():
    request_data = request.get_json()
    for user in USERS:
        if user['id'] == int(request_data['id']):
           user['name'] = request_data['name']
    return jsonify({"status": "ok"})

@app.route("/user/<int:id>", methods=['DELETE'])
def del_user_by_id(id):
    for user in USERS:
        if user['id'] == int(id):
            USERS.remove(user)
    return jsonify({"status": "ok"})

@app.route("/user/<name>", methods=['DELETE'])
def del_user_by_name(name):
    for user in USERS:
        if user['name'] == name:
            USERS.remove(user)
    return jsonify({"status": "ok"})



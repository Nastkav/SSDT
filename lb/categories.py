from flask import jsonify, request
from lb import app

CATEGORIES = [
    {
        "id": 1,
        "name": "Food",
    },
    {
        "id": 2,
        "name": "Health",
    }
]


# GET /CATEGORIES
# POST /CATEGORY
@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['POST'])
def create_category():
    request_data = request.get_json()
    CATEGORIES.append(request_data)
    return jsonify({"status": "ok"})

@app.route("/category", methods=['PUT'])
def change_category():
    request_data = request.get_json()
    for category in CATEGORIES:
        if category['id'] == int(request_data['id']):
           category['name'] = request_data['name']
    return jsonify({"status": "ok"})


@app.route("/category/<int:id>", methods=['DELETE'])
def del_category_by_id(id):
    for category in CATEGORIES:
        if category['id'] == int(id):
            CATEGORIES.remove(category)
    return jsonify({"status": "ok"})


@app.route("/category/<name>", methods=['DELETE'])
def del_category_by_name(name):
    for category in CATEGORIES:
        if category['name'] == name:
            CATEGORIES.remove(category)
    return jsonify({"status": "ok"})

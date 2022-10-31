from flask import jsonify, request
from lb import app

NOTES = [
    {
        "id": 1,
        "id_user": 2,
        "id_category": 1,
        "date": "04-11-2022",
        "sum": 320
    },
    {
        "id": 2,
        "id_user": 1,
        "id_category": 2,
        "date": "05-12-2022",
        "sum": 480
    }
]

@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})


@app.route("/note", methods=['POST'])
def create_note():
    request_data = request.get_json()
    NOTES.append(request_data)
    return jsonify({"status": "ok"})

@app.route("/note", methods=['PUT'])
def change_note():
    request_data = request.get_json()
    for note in NOTES:
        if note['id'] == int(request_data['id']):
           note["id_user"] = request_data["id_user"]
           note["id_category"] = request_data["id_category"]
           note["date"] = request_data["date"]
           note["sum"] = request_data["sum"]
    return jsonify({"status": "ok"})


@app.route("/note/<int:id>", methods=['DELETE'])
def del_note_by_id(id):
    for note in NOTES:
        if note['id'] == int(id):
            NOTES.remove(note)
    return jsonify({"status": "ok"})


@app.route("/note/<date>", methods=['DELETE'])
def del_note_by_date(date):
    for note in NOTES:
        if note['date'] == date:
            NOTES.remove(note)
    return jsonify({"status": "ok"})
from flask import request, jsonify, abort
from app import app

ENTRIES = [
    {
        'id': 1,
        'title': 'again i did it',
        'journal': 'always away from it'
    }
]


@app.route('/api/v1/entries', methods=['POST'])
def create_entry():
    """
    Create an entry into the journal endpoint
    201 response
    """
    # parse entry to json
    req_data = request.get_json()
    entry = {
        'id': ENTRIES[-1]['id'] + 1,
        'title': req_data['title'],
        'journal': req_data['journal'],
    }
    ENTRIES.append(entry)
    return jsonify({'entries': ENTRIES}), 201


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    """
    Endpoint to get all the entries in the diary
    success is 200
    """
    return jsonify({'entries': ENTRIES}), 200


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_entry_id(entry_id):
    """
     Endpoint to get an entry by id
    """
    # create a list of one item = entry specified
    entry = [entry for entry in ENTRIES if entry['id'] == entry_id]
    if not entry:
        abort(404)
    return jsonify({'entry': entry[0]}), 200

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


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_an_entry(entry_id):
    """
    Endpoint to modify and entry
    """
    # put the entry in the list with the the specific id
    # abort if not found
    entry = [entry for entry in ENTRIES if entry['id'] == entry_id]
    if not entry:
        abort(404)

    req_data = request.get_json()

    # check if entry doesnt contain both title and journal
    # abort if none with a not found
    if 'title' and 'journal' not in req_data:
        abort(404)
    # abort with bad request when title and journal or both
    # are not strings
    if 'title' in req_data and not isinstance(req_data['title'], str):
        abort(400)
    if 'journal' in req_data and not isinstance(req_data['journal'], str):
        abort(400)

    entry[0]['title'] = req_data['title']
    entry[0]['journal'] = req_data['journal']
    return jsonify({'entry': entry[0]}), 201

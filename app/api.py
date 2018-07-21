from flask import request, jsonify
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

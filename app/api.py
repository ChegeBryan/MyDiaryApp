"""Defines the api endpoints"""

from flask import request, jsonify, abort
from app import app
from flask.views import MethodView

ENTRIES = [
    {
        'id': 1,
        'title': 'again i did it',
        'journal': 'always away from it'
    }
]


class EntryAPI(MethodView):
    """Class implements the api endpoints using Methodvieww"""

    def get(self, entry_id):
        """
        Endpoint to get all the entries in the diary if no id supplied
        else return a specific entry
        :return 200 success
        :return 404 no entry found
        """

        if entry_id is None:
            return jsonify({'entries': ENTRIES}), 200
        else:
            # create a list of one item = entry specified
            entry = [entry for entry in ENTRIES if entry['id'] == entry_id]
            if not entry:
                abort(404)
            return jsonify({'entry': entry[0]}), 200

    def post(self):
        """
        Create an entry into the journal
        :return 201 Created OK
        """
        # parse entry to json
        request_data = request.get_json()
        entry = {
            'id': ENTRIES[-1]['id'] + 1,
            'title': request_data['title'],
            'journal': request_data['journal'],
        }
        ENTRIES.append(entry)
        return jsonify({'entries': ENTRIES}), 201

    def put(self, entry_id):
        """
        Endpoint to modify and entry
        """
        # put the entry in the list with the the specific id
        # abort if not found
        entry = [entry for entry in ENTRIES if entry['id'] == entry_id]
        if not entry:
            abort(404)

        request_data = request.get_json()

        # check if entry doesnt contain both title and journal
        # abort if none with a not found
        if 'title' and 'journal' not in request_data:
            abort(404)
        # abort with bad request when title and journal or both
        # are not strings
        if 'title' in request_data and not isinstance(request_data['title'], str):
            abort(400)
        if 'journal' in request_data and not isinstance(request_data['journal'], str):
            abort(400)

        entry[0]['title'] = request_data['title']
        entry[0]['journal'] = request_data['journal']
        return jsonify({'entry': entry[0]}), 201


entry_api_view = EntryAPI.as_view('entry_api')
app.add_url_rule('/api/v1/entries', defaults={'entry_id': None},
                 view_func=entry_api_view, methods=['GET'])
app.add_url_rule('/api/v1/entries', view_func=entry_api_view, methods=['POST'])
app.add_url_rule('/api/v1/entries/<int:entry_id>', view_func=entry_api_view,
                 methods=['GET', 'PUT'])
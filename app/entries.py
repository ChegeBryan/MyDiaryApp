"""Defines the api endpoints"""

from flask import request, jsonify, abort
from app import app
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.models import Entry


class EntryAPI(MethodView):
    """Class implements the api endpoints using GET, POST, PUT"""
    @jwt_required
    def post(self):
        """
        Create an entry into the journal
        :return 201 Created OK
        """
        # parse entry to json
        request_data = request.get_json()
        if 'title' not in request_data:
            return jsonify({'message': 'missing data in json request'}), 400
        if 'journal' not in request_data:
            return jsonify({'message': 'Missing data in json request'}), 400
        if 'title' in request_data and not request_data['title'].strip():
            return jsonify({'message': 'title cannot be empty'}), 400
        if 'journal' in request_data and not request_data['journal'].strip():
            return jsonify({'message': 'journal cannot be empty'}), 400
        title = request_data['title']
        journal = request_data['journal']
        created_by = get_jwt_identity()
        entry = Entry(user_id=created_by, title=title, journal=journal)
        entry.add_entry()
        return jsonify({'message': 'entry saved'}), 201

    @jwt_required
    def get(self):
        """
        Endpoint to get all the entries in the diary if for the user who is logged in
        :return 200 success
        :return 404 no entry found
        """
        user_id = get_jwt_identity()
        entries = Entry.get_entries(user_id)
        print(entries)
        return jsonify({'message': entries}), 200

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
app.add_url_rule('/api/v1/entries', view_func=entry_api_view, methods=['GET'])
app.add_url_rule('/api/v1/entries', view_func=entry_api_view, methods=['POST'])
app.add_url_rule('/api/v1/entries/<int:entry_id>', view_func=entry_api_view,
                 methods=['GET', 'PUT'])


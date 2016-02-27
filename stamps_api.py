#!flask/bin/python

"""
Description: This API is part of the Thinkful Stamps project.
The API is to allow for GET requests that will fetch populated data and save that data in a JSON object.

POST, UPDATE & DELETE requests will come as the data categories are flushed out.
authored by Michael Nickey on February 26th 2016
"""

from flask import Flask, jsonify, abort
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

version = 1
stamps = [
    {
        "id": 1,
        "name": "My first stamp",
        "orgin": "Unicorn Nightmares",
        "rarity": "very rare"
    },
    {
        "id": 2,
        "name": "My second Stanp",
        "orgin": "Heavens Breath",
        "rarity": "common"
    }
]


# Get all the stamps
@app.route('/api/stamps/', methods=['GET'])
def get_stamps():
    return jsonify({'stamps': stamps[:]})


# Get the stamp by stamp ID
@app.route('/api/stamps/<int:stamp_id>/', methods=['GET'])
def get_stamps_by_id(stamp_id):
    logger.info('\nCollecting matching stamp...')
    stamp = [stamp for stamp in stamps if stamp['id'] == stamp_id]
    if len(stamp) == 0:
        abort(404)
    return jsonify({'stamps': stamp})

if __name__ == '__main__':
    app.run(debug=True)

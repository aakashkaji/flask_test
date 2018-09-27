from flask import Blueprint, request, abort, jsonify


sheet_blueprint = Blueprint('routes', __name__)


@sheet_blueprint.route('/index', methods=['POST', 'GET'])
def mytest():

    return jsonify({"response": "hi aakash ", "status": "ok"})
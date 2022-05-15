# For routes pertaining to our Bencos

from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from models.benco import Benco
from repositories.benco_repo import BencoRepo
from services.benco_service import BencoService

br = BencoRepo()
bs = BencoService(br)


def route(app):
    # @app.route("/bc_login", methods=['GET', 'POST'])
    # def bc_login():
    #     pass

    @app.route("/bencos", methods=['GET'])
    def get_all_bencos():
        return jsonify([benco.json() for benco in bs.get_all_bencos()])

    @app.route("/bencos/<bc_id>", methods=['GET'])
    def get_benco(bc_id):
        try:
            return bs.get_benco_by_id(int(bc_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/bencos", methods=['POST'])
    def post_benco():
        try:
            body = request.json

            benco = Benco(name=body["name"])
            benco = bs.create_benco(benco)
            return benco.json(), 201
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/bencos/", methods=["PUT"])
    def put_benco():
        body = request.json

        benco = Benco(bc_id=body["bcId"], name=body["name"])
        benco = bs.update_benco(benco)

        return benco.json()

    @app.route("/bencos/<bc_id>", methods=["DELETE"])
    def delete_benco(bc_id):
        try:
            bs.delete_benco(bc_id)
            return "Benefits Coordinator successfully deleted", 204
        except ResourceNotFound as r:
            return r.message, 404

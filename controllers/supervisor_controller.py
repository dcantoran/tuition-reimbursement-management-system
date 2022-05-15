# For routes pertaining to our Supervisors

from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from models.supervisor import Supervisor
from repositories.supervisor_repo import SupervisorRepo
from services.supervisor_service import SupervisorService

svr = SupervisorRepo()
svs = SupervisorService(svr)


def route(app):
    @app.route("/supervisors", methods=['GET'])
    def get_all_supervisors():
        return jsonify([supervisor.json() for supervisor in svs.get_all_supervisors()])

    @app.route("/supervisors/<sv_id>", methods=['GET'])
    def get_supervisor(sv_id):
        try:
            return svs.get_supervisor_by_id()(int(sv_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/supervisors", methods=['POST'])
    def post_supervisor():
        body = request.json

        supervisor = Supervisor(name=body["name"], is_dh=body["isDh"])
        supervisor = svs.create_supervisor(supervisor)
        return supervisor.json()

    @app.route("/supervisors/<sv_id>", methods=["PUT"])
    def put_supervisor(sv_id):
        body = request.json

        supervisor = Supervisor(sv_id=sv_id, name=body["name"], is_dh=body["isDh"])
        supervisor = svs.update_supervisor(supervisor)

        return supervisor.json()

    @app.route("/supervisors/<sv_id>", methods=["DELETE"])
    def delete_supervisor(sv_id):
        try:
            svs.delete_supervisor(sv_id)
            return f"Supervisor {sv_id} successfully deleted", 204
        except ResourceNotFound as r:
            return r.message, 404

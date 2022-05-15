# For routes pertaining to our Supervisors

from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from models.applicant import Applicant
from repositories.applicant_repo import ApplicantRepo
from services.applicant_service import ApplicantService

ar = ApplicantRepo()
aps = ApplicantService(ar)


def route(app):
    @app.route("/applicants", methods=['GET'])
    def get_all_applicants():
        return jsonify([applicant.json() for applicant in aps.get_all_applicants()])

    @app.route("/applicants/<a_id>", methods=['GET'])
    def get_applicant(a_id):
        try:
            return aps.get_applicant_by_id()(int(a_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/applicants", methods=['POST'])
    def post_applicant():
        body = request.json

        applicant = Applicant(name=body["name"], benco_id=body["bencoId"],
                              depthead_id=body["deptheadId"], super_id=body["superId"])
        applicant = aps.create_applicant(applicant)
        return applicant.json()

    @app.route("/applicants/<a_id>", methods=["PUT"])
    def put_applicant(a_id):
        body = request.json

        applicant = Applicant(a_id=a_id, name=body["name"], benco_id=body["bencoId"],
                              depthead_id=body["deptheadId"], super_id=body["superId"])
        applicant = aps.update_applicant(applicant)

        return applicant.json()

    @app.route("/applicants/<a_id>", methods=["DELETE"])
    def delete_applicant(a_id):
        try:
            aps.delete_applicant(a_id)
            return f"Applicant {a_id} successfully deleted", 204
        except ResourceNotFound as r:
            return r.message, 404

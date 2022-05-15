# For routes pertaining to our Supervisors

from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from repositories.form_repo import FormRepo
from services.form_service import FormService
from datetime import time

fr = FormRepo()
fs = FormService(fr)


def route(app):
    @app.route("/forms", methods=['GET'])
    def get_all_forms():
        return jsonify([form.json() for form in fs.get_all_forms()])

    @app.route("/forms/<f_id>", methods=['GET'])
    def get_form(f_id):
        try:
            return fs.get_form_by_id(int(f_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/forms", methods=['POST'])
    def post_form():
        body = request.json

        form = Form(a_name=body["aName"], location=body["location"], description=body["description"],
                    e_cost=body["eCost"], e_type=body["eType"], grade_format=body["gradeFormat"], app_id=body["appId"])
        form = fs.create_form(form)
        return form.json()

    @app.route("/forms/", methods=["PUT"])
    def put_form():
        body = request.json

        form = Form(f_id=body["fId"], a_name=body["aName"])
        form = fs.update_form(form)

        return form.json()

    @app.route("/forms/<f_id>", methods=["DELETE"])
    def delete_form(f_id):
        try:
            fs.delete_form(f_id)
            return f"Form {f_id} successfully deleted", 204
        except ResourceNotFound as r:
            return r.message, 404


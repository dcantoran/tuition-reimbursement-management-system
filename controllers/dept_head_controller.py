# For routes pertaining to our Department Heads

from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from models.dept_head import DeptHead
from repositories.dept_head_repo import DeptHeadRepo
from services.dept_head_service import DeptHeadService

dhr = DeptHeadRepo()
ds = DeptHeadService(dhr)


def route(app):
    @app.route("/deptheads", methods=['GET'])
    def get_all_dept_heads():
        return jsonify([dept_head.json() for dept_head in ds.get_all_dept_heads()])

    @app.route("/deptheads/<dh_id>", methods=['GET'])
    def get_dept_head(dh_id):
        try:
            return ds.get_dept_head_by_id(int(dh_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/deptheads", methods=['POST'])
    def post_dept_head():
        body = request.json

        dept_head = DeptHead(name=body["name"])
        dept_head = ds.create_dept_head(dept_head)
        return dept_head.json()

    @app.route("/deptheads/<dh_id>", methods=["PUT"])
    def put_dept_head(dh_id):
        body = request.json

        dept_head = DeptHead(dh_id=dh_id, name=body["name"])
        dept_head = ds.update_dept_head(dept_head)

        return dept_head.json()

    @app.route("/deptheads/<dh_id>", methods=["DELETE"])
    def delete_dept_head(dh_id):
        try:
            ds.delete_dept_head(dh_id)
            return f"Department Head {dh_id} successfully deleted", 204
        except ResourceNotFound as r:
            return r.message, 404

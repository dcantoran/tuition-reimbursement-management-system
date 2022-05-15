from controllers import home_controller, benco_controller, dept_head_controller, supervisor_controller, \
    applicant_controller, form_controller


def route(app):
    home_controller.route(app)
    benco_controller.route(app)
    dept_head_controller.route(app)
    supervisor_controller.route(app)
    applicant_controller.route(app)
    form_controller.route(app)
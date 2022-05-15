# Form Model -> Reflect the Form Table in my DB
class Form:

    def __init__(self, f_id=0, a_name="", date_submitted="", time_submitted="", location="", description="",
                 e_cost=0, e_type="", e_status="", grade_format="", bc_approved=None, dh_approved=None,
                 sv_approved=None, app_id=0):
        self.f_id = f_id
        self.a_name = a_name
        self.date_submitted = date_submitted
        self.time_submitted = time_submitted
        self.location = location
        self.description = description
        self.e_cost = e_cost
        self.e_type = e_type
        self.e_status = e_status
        self.grade_format = grade_format
        self.bc_approved = bc_approved
        self.dh_approved = dh_approved
        self.sv_approved = sv_approved
        self.app_id = app_id

    # Dunder "repr" for how to print something to a string
    def __repr__(self):
        return str({
            'f_id': self.f_id,
            'a_name': self.a_name,
            'date_submitted': self.date_submitted,
            'time_submitted': self.time_submitted,
            'location': self.location,
            'description': self.description,
            'e_cost': self.e_cost,
            'e_type': self.e_type,
            'e_status': self.e_status,
            'grade_format': self.grade_format,
            'bc_approved': self.bc_approved,
            'dh_approved': self.dh_approved,
            'sv_approved': self.sv_approved,
            'app_id': self.app_id
        })

    def json(self):
        return {
            'fId': self.f_id,
            'aName': self.a_name,
            'dateSubmitted': self.date_submitted,
            'timeSubmitted': self.time_submitted,
            'location': self.location,
            'description': self.description,
            'eCost': self.e_cost,
            'eType': self.e_type,
            'eStatus': self.e_status,
            'gradeFormat': self.grade_format,
            'bcApproved': self.bc_approved,
            'dhApproved': self.dh_approved,
            'svApproved': self.sv_approved,
            'appId': self.app_id
        }
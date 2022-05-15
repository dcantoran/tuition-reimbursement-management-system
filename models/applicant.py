# Applicant Model -> Reflect the Applicant Table in my DB
class Applicant:

    def __init__(self, a_id=0, name="", benco_id=0, depthead_id=0, super_id=0):
        self.a_id = a_id
        self.name = name
        self.benco_id = benco_id
        self.depthead_id = depthead_id
        self.super_id = super_id

    def __repr__(self):
        return str({
            'a_id': self.a_id,
            'name': self.name,
            'benco_id': self.benco_id,
            'depthead_id': self.depthead_id,
            'super_id': self.super_id
        })

    def json(self):
        return {
            'aId': self.a_id,
            'name': self.name,
            'bencoId': self.benco_id,
            'deptheadId': self.depthead_id,
            'superId': self.super_id
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Applicant):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

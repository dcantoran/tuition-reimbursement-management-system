# DeptHead Model -> Reflect the DeptHead Table in my DB
class DeptHead:

    def __init__(self, dh_id=0, name=""):
        self.dh_id = dh_id
        self.name = name

    def __repr__(self):
        return str({
            'dh_id': self.dh_id,
            'name': self.name
        })

    def json(self):
        return {
            'dhId': self.dh_id,
            'name': self.name
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, DeptHead):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

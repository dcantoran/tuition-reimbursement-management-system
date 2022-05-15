# BenCo Model -> Reflect the BenCo Table in my DB
class Benco:

    def __init__(self, bc_id=0, name=""):
        self.bc_id = bc_id
        self.name = name

    def __repr__(self):
        return str({
            'bc_id': self.bc_id,
            'name': self.name
        })

    def json(self):
        return {
            'bcId': self.bc_id,
            'name': self.name
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Benco):
            return False
        # programmatic approach to line 33 of __dict__ comparison
        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False
        #
        # return True
        return self.__dict__ == other.__dict__

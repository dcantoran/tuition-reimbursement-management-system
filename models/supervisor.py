# Supervisor Model -> Reflect the Supervisor Table in my DB
class Supervisor:

    def __init__(self, sv_id=0, name="", is_dh=False):
        self.sv_id = sv_id
        self.name = name
        self.is_dh = is_dh

    def __repr__(self):
        return str({
            'sv_id': self.sv_id,
            'name': self.name,
            'is_dh': self.is_dh
        })

    def json(self):
        return {
            'svId': self.sv_id,
            'name': self.name,
            'isDh': self.is_dh
        }
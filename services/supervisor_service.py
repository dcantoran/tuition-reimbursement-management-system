from exceptions.resource_unavailable import ResourceUnavailable
from repositories.supervisor_repo import SupervisorRepo


class SupervisorService:

    def __init__(self, svr: SupervisorRepo):
        self.svr = svr

    def create_supervisor(self, supervisor):
        return self.svr.create_supervisor(supervisor)

    def get_supervisor_by_id(self, sv_id):
        return self.svr.get_supervisor(sv_id)

    def get_all_supervisors(self):
        return self.svr.all_supervisors()

    def update_supervisor(self, change):
        return self.svr.update_supervisor(change)

    def delete_supervisor(self, sv_id):
        return self.svr.delete_supervisor(sv_id)


def _test():
    svr = SupervisorRepo()
    svs: SupervisorService = SupervisorService(svr)

    print(svs.get_all_supervisors())


if __name__ == '__main__':
    _test()
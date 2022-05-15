from exceptions.resource_unavailable import ResourceUnavailable
from repositories.dept_head_repo import DeptHeadRepo


class DeptHeadService:

    def __init__(self, dhr: DeptHeadRepo):
        self.dhr = dhr

    def create_dept_head(self, dept_head):
        return self.dhr.create_dept_head(dept_head)

    def get_dept_head_by_id(self, dh_id):
        return self.dhr.get_dept_head(dh_id)

    def get_all_dept_heads(self):
        return self.dhr.all_dept_heads()

    def update_dept_head(self, change):
        return self.dhr.update_dept_head(change)

    def delete_dept_head(self, bc_id):
        return self.dhr.delete_dept_head(bc_id)


def _test():
    dhr = DeptHeadRepo()
    dhs: DeptHeadService = DeptHeadService(dhr)

    print(dhs.get_all_dept_heads())


if __name__ == '__main__':
    _test()
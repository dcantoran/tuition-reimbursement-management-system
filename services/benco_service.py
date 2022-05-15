# from exceptions.resource_unavailable import ResourceUnavailable
from repositories.benco_repo import BencoRepo


class BencoService:

    def __init__(self, bcr: BencoRepo):
        self.bcr = bcr

    def create_benco(self, benco):
        return self.bcr.create_benco(benco)

    def get_benco_by_id(self, bc_id):
        return self.bcr.get_benco(bc_id)

    def get_all_bencos(self):
        return self.bcr.all_bencos()

    def update_benco(self, change):
        return self.bcr.update_benco(change)

    def delete_benco(self, bc_id):
        return self.bcr.delete_benco(bc_id)


def _test():
    bcr = BencoRepo()
    bcs: BencoService = BencoService(bcr)

    print(bcs.get_all_bencos())


if __name__ == '__main__':
    _test()
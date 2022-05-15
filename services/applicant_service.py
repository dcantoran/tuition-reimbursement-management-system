from exceptions.resource_unavailable import ResourceUnavailable
from repositories.applicant_repo import ApplicantRepo


class ApplicantService:

    def __init__(self, ar: ApplicantRepo):
        self.ar = ar

    def create_applicant(self, applicant):
        return self.ar.create_applicant(applicant)

    def get_applicant_by_id(self, a_id):
        return self.ar.get_applicant(a_id)

    def get_all_applicants(self):
        return self.ar.all_applicants()

    def update_applicant(self, change):
        return self.ar.update_applicant(change)

    def delete_applicant(self, a_id):
        return self.ar.delete_applicant(a_id)


def _test():
    ar = ApplicantRepo()
    aps: ApplicantService = ApplicantService(ar)

    print(aps.get_all_applicants())


if __name__ == '__main__':
    _test()
from exceptions.resource_unavailable import ResourceUnavailable
from repositories.form_repo import FormRepo
from datetime import time


class FormService:

    def __init__(self, fr: FormRepo):
        self.fr = fr

    def create_form(self, form):
        return self.fr.create_form(form)

    def get_form_by_id(self, f_id):
        return self.fr.get_form(f_id)

    def get_all_forms(self):
        return self.fr.all_forms()

    def get_all_forms_by_applicant_id(self, app_id):
        return self.fr.all_forms_by_applicant_id(app_id)

    def get_all_forms_by_applicant_benco_id(self, benco_id):
        return self.fr.all_forms_by_applicant_benco_id(benco_id)

    def get_all_forms_by_applicant_depthead_id(self, depthead_id):
        return self.fr.all_forms_by_applicant_depthead_id(depthead_id)

    def get_all_forms_by_applicant_super_id(self, super_id):
        return self.fr.all_forms_by_applicant_super_id(super_id)

    def update_form(self, change):
        return self.fr.update_form(change)

    def delete_form(self, f_id):
        return self.fr.delete_form(f_id)


def _test():
    fr = FormRepo()
    fs: FormService = FormService(fr)

    print(fs.get_all_forms())
    # print(fs.get_form_by_id(1))
    # print(fs.get_all_forms_by_applicant_super_id(1))


if __name__ == '__main__':
    _test()
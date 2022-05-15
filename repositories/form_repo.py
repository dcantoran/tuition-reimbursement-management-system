from datetime import datetime

from exceptions.resource_not_found import ResourceNotFound
from models.form import Form
from util.db_connection import connection


def _build_form(record):
    return Form(f_id=record[0], a_name=record[1], date_submitted=record[2], time_submitted=record[3],
                location=record[4], description=record[5], e_cost=record[6], e_type=record[7], e_status=record[8],
                grade_format=record[9], bc_approved=record[10], dh_approved=record[11], sv_approved=record[12],
                app_id=record[13])


class FormRepo:
    # Issue: Creating a form with a non-existent 'app_id' gives me an f_key error. The applicant needs to exist so
    # Option A: I create a 'create_applicant_by_form' where once I create the form I also create a new applicant
    # Option B: Give 'app_id' a NULL value and edit the 'app_id' in an UPDATE method instead
    #           I'd need to create the applicant before creating a form for Option 'B'
    def create_form(self, form):
        sql = "INSERT INTO form VALUES (DEFAULT, %s, DEFAULT, DEFAULT, %s, %s, %s, %s, DEFAULT, %s, " \
              "NULL, NULL, NULL, %s) RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [form.a_name, form.location, form.description, form.e_cost,
                          form.e_type, form.grade_format, form.app_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def get_form(self, f_id):
        sql = "SELECT * FROM form WHERE f_id = %s"
        cur = connection.cursor()

        cur.execute(sql, [f_id])

        record = cur.fetchone()
        # record_list = list(record)
        # print(record_list)
        # for r in record_list:
        # print(str(record_list[3]))

        if record:
            return _build_form(record)
        else:
            raise ResourceNotFound(f"Form with id {f_id} - Not Found")

    def all_forms(self):
        sql = "SELECT * FROM form"
        cur = connection.cursor()
        cur.execute(sql)

        records = cur.fetchall()

        form_list = [_build_form(record) for record in records]

        # for i in records:
        #     client_list.append(i)
        return form_list

    def all_forms_by_applicant_id(self, app_id):
        sql = "SELECT * FROM form WHERE app_id = %s"
        cur = connection.cursor()
        cur.execute(sql, [app_id])

        records = cur.fetchall()

        form_list = [_build_form(record) for record in records]
        return form_list

    def all_forms_by_applicant_benco_id(self, benco_id):
        sql = "SELECT * FROM form LEFT JOIN applicant ON form.app_id = applicant.a_id WHERE applicant.benco_id = %s;"
        cur = connection.cursor()
        cur.execute(sql, [benco_id])

        records = cur.fetchall()

        form_list = [_build_form(record) for record in records]
        return form_list

    def all_forms_by_applicant_depthead_id(self, depthead_id):
        sql = "SELECT * FROM form LEFT JOIN applicant ON form.app_id = applicant.a_id WHERE applicant.depthead_id = %s;"
        cur = connection.cursor()
        cur.execute(sql, [depthead_id])

        records = cur.fetchall()

        form_list = [_build_form(record) for record in records]
        return form_list

    def all_forms_by_applicant_super_id(self, super_id):
        sql = "SELECT * FROM form LEFT JOIN applicant ON form.app_id = applicant.a_id WHERE applicant.super_id = %s;"
        cur = connection.cursor()
        cur.execute(sql, [super_id])

        records = cur.fetchall()

        form_list = [_build_form(record) for record in records]
        return form_list

    def update_form(self, change):
        sql = "UPDATE form SET a_name = %s WHERE f_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.a_name, change.f_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def update_form_approval(self, change):
        sql = "UPDATE form SET e_status = %s, bc_approved = %s, dh_approved = %s, sv_approved = %s " \
              "WHERE f_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.e_status, change.bc_approved, change.dh_approved, change.sv_approved, change.f_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def update_form_approval_by_benco_id(self, benco_id, a_id):
        sql = "UPDATE form SET bc_approved = true FROM applicant WHERE form.app_id = applicant.a_id " \
              "AND applicant.benco_id = %s AND applicant.a_id = %s;"

        cur = connection.cursor()
        cur.execute(sql, [benco_id, a_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def update_form_approval_by_depthead_id(self, depthead_id, a_id):
        sql = "UPDATE form SET dh_approved = true FROM applicant WHERE form.app_id = applicant.a_id " \
              "AND applicant.depthead_id = %s AND applicant.a_id = %s;"

        cur = connection.cursor()
        cur.execute(sql, [depthead_id, a_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def update_form_approval_by_super_id(self, super_id, a_id):
        sql = "UPDATE form SET sv_approved = true FROM applicant WHERE form.app_id = applicant.a_id " \
              "AND applicant.super_id = %s AND applicant.a_id = %s;"

        cur = connection.cursor()
        cur.execute(sql, [super_id, a_id])

        connection.commit()
        record = cur.fetchone()

        return _build_form(record)

    def delete_form(self, f_id):
        sql = "DELETE FROM form WHERE f_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [f_id])
        connection.commit()
        record = cur.fetchone()
        # Need this to handle raise
        if not record:
            raise ResourceNotFound(f"No record with id {f_id}")


def _test():
    fr = FormRepo()
    print("--------- ALL FORMS --------")
    all_forms = fr.all_forms()
    print(all_forms)
    # print(fr.all_forms_by_applicant_id(2))
    # print(fr.all_forms_by_applicant_depthead_id(2))
    # f1 = fr.get_form(1)
    # f1.e_status = "approved"
    # f1 = fr.update_form(f1)
    # print(f1)

    # test_obj = Form(a_name="Will", location='Denver', description='4th Description', e_cost=5000,
    #                 e_type='Univ Courses', grade_format='presentation', app_id=4)
    # fr.create_form(test_obj)
    # fr.delete_form(5)
    # all_forms = fr.all_forms()
    # print(all_forms)


if __name__ == '__main__':
    _test()
from exceptions.resource_not_found import ResourceNotFound
from models.applicant import Applicant
from util.db_connection import connection


def _build_applicant(record):
    return Applicant(a_id=record[0], name=record[1], benco_id=record[2],
                     depthead_id=record[3], super_id=record[4])


class ApplicantRepo:

    def create_applicant(self, app):
        sql = "INSERT INTO applicant VALUES (DEFAULT, %s, %s, %s, %s) RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [app.name, app.benco_id, app.depthead_id, app.super_id])

        connection.commit()
        record = cur.fetchone()

        return _build_applicant(record)

    def get_applicant(self, a_id):
        sql = "SELECT * FROM applicant WHERE a_id = %s"
        cur = connection.cursor()

        cur.execute(sql, [a_id])

        record = cur.fetchone()

        if record:
            return _build_applicant(record)
        else:
            raise ResourceNotFound(f"Dept. Head with id {a_id} - Not Found")

    def all_applicants(self):
        sql = "SELECT * FROM applicant"
        cur = connection.cursor()
        cur.execute(sql)

        records = cur.fetchall()

        applicant_list = [_build_applicant(record) for record in records]

        # for i in records:
        #     client_list.append(i)
        return applicant_list

    def update_applicant(self, change):
        sql = "UPDATE applicant SET name = %s WHERE a_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.name, change.a_id])

        connection.commit()
        record = cur.fetchone()

        return _build_applicant(record)

    def delete_applicant(self, a_id):
        sql = "DELETE FROM applicant WHERE a_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [a_id])
        connection.commit()
        record = cur.fetchone()
        # Need this to handle raise
        if not record:
            raise ResourceNotFound(f"No record with id {a_id}")


def _test():
    ar = ApplicantRepo()
    print("--------- ALL APPLICANTS --------")
    # all_applicants = ar.all_applicants()
    # print(all_applicants)
    # a1 = ar.get_applicant(1)
    # a1.name = "Luke"
    # a1 = ar.update_applicant(a1)
    # print(a1)

    # test_obj = Applicant(name="Will", benco_id=5, depthead_id=5, super_id=5)
    # ar.create_applicant(test_obj)
    ar.delete_applicant(6)
    all_applicants = ar.all_applicants()
    print(all_applicants)


if __name__ == '__main__':
    _test()
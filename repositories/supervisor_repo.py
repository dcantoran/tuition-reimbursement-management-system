from exceptions.resource_not_found import ResourceNotFound
from models.supervisor import Supervisor
from util.db_connection import connection


def _build_supervisor(record):
    return Supervisor(sv_id=record[0], name=record[1], is_dh=record[2])


class SupervisorRepo:

    def create_supervisor(self, supervisor):
        sql = "INSERT INTO supervisor VALUES (DEFAULT, %s, NULL) RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [supervisor.name])

        connection.commit()
        record = cur.fetchone()

        return _build_supervisor(record)

    def get_supervisor(self, sv_id):
        sql = "SELECT * FROM supervisor WHERE sv_id = %s"
        cur = connection.cursor()

        cur.execute(sql, [sv_id])

        record = cur.fetchone()

        if record:
            return _build_supervisor(record)
        else:
            raise ResourceNotFound(f"Supervisor with id {sv_id} - Not Found")

    def all_supervisors(self):
        sql = "SELECT * FROM supervisor"
        cur = connection.cursor()
        cur.execute(sql)

        records = cur.fetchall()

        supervisor_list = [_build_supervisor(record) for record in records]

        # for i in records:
        #     client_list.append(i)
        return supervisor_list

    def update_supervisor(self, change):
        sql = "UPDATE supervisor SET name = %s, is_dh = %s WHERE sv_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.name, change.is_dh, change.sv_id])

        connection.commit()
        record = cur.fetchone()

        return _build_supervisor(record)

    def delete_supervisor(self, sv_id):
        sql = "DELETE FROM supervisor WHERE sv_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [sv_id])
        connection.commit()
        record = cur.fetchone()
        # Need this to handle raise
        if not record:
            raise ResourceNotFound(f"No record with id {sv_id}")


def _test():
    sr = SupervisorRepo()
    print("--------- ALL SUPERVISORS --------")
    all_supervisors = sr.all_supervisors()
    print(all_supervisors)
    sv1 = sr.get_supervisor(1)
    # sv1.name = "Vince"
    # sv1 = sr.update_supervisor(sv1)
    print(sv1)

    # test_obj = Supervisor(name="Grey")
    # sr.create_supervisor(test_obj)
    # sr.delete_supervisor(4)
    # all_supervisors = sr.all_supervisors()
    # print(all_supervisors)


if __name__ == '__main__':
    _test()
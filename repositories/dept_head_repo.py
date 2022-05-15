from exceptions.resource_not_found import ResourceNotFound
from models.dept_head import DeptHead
from util.db_connection import connection


def _build_dept_head(record):
    return DeptHead(dh_id=record[0], name=record[1])


class DeptHeadRepo:

    def create_dept_head(self, dept_head):
        sql = "INSERT INTO dept_head VALUES (DEFAULT, %s) RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [dept_head.name])

        connection.commit()
        record = cur.fetchone()

        return _build_dept_head(record)

    def get_dept_head(self, dh_id):
        sql = "SELECT * FROM dept_head WHERE dh_id = %s"
        cur = connection.cursor()

        cur.execute(sql, [dh_id])

        record = cur.fetchone()

        if record:
            return _build_dept_head(record)
        else:
            raise ResourceNotFound(f"Dept. Head with id {dh_id} - Not Found")

    def all_dept_heads(self):
        sql = "SELECT * FROM dept_head"
        cur = connection.cursor()
        cur.execute(sql)

        records = cur.fetchall()

        dept_head_list = [_build_dept_head(record) for record in records]

        # for i in records:
        #     client_list.append(i)
        return dept_head_list

    def update_dept_head(self, change):
        sql = "UPDATE dept_head SET name = %s WHERE dh_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.name, change.dh_id])

        connection.commit()
        record = cur.fetchone()

        return _build_dept_head(record)

    def delete_dept_head(self, dh_id):
        sql = "DELETE FROM dept_head WHERE dh_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [dh_id])
        connection.commit()
        record = cur.fetchone()
        # Need this to handle raise
        if not record:
            raise ResourceNotFound(f"No record with id {dh_id}")


def _test():
    dhr = DeptHeadRepo()
    print("--------- ALL DEPT HEADS --------")
    all_dept_heads = dhr.all_dept_heads()
    print(all_dept_heads)
    dh1 = dhr.get_dept_head(1)
    # dh1.name = "Ryan"
    # dh1 = dhr.update_dept_head(dh1)
    print(dh1)

    # test_obj = DeptHead(name="Grey")
    # dhr.create_dept_head(test_obj)
    # dhr.delete_dept_head(4)
    # all_dept_heads = dhr.all_dept_heads()
    # print(all_dept_heads)


if __name__ == '__main__':
    _test()
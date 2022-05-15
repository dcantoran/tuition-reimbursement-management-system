from exceptions.resource_not_found import ResourceNotFound
from models.benco import Benco
from util.db_connection import connection


def _build_benco(record):
    if record:
        return Benco(bc_id=record[0], name=record[1])
    else:
        return None


class BencoRepo:

    def create_benco(self, benco):
        sql = "INSERT INTO benco VALUES (DEFAULT, %s) RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [benco.name])

        connection.commit()
        record = cur.fetchone()

        return _build_benco(record)

    def get_benco(self, bc_id):
        sql = "SELECT * FROM benco WHERE bc_id = %s"
        cur = connection.cursor()

        cur.execute(sql, [bc_id])

        record = cur.fetchone()

        if record:
            return _build_benco(record)
        else:
            raise ResourceNotFound(f"Benco with id {bc_id} - Not Found")

    def all_bencos(self):
        sql = "SELECT * FROM benco"
        cur = connection.cursor()
        cur.execute(sql)

        records = cur.fetchall()

        benco_list = [_build_benco(record) for record in records]

        # for i in records:
        #     client_list.append(i)
        return benco_list

    def update_benco(self, change):
        sql = "UPDATE benco SET name = %s WHERE bc_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [change.name, change.bc_id])

        connection.commit()
        record = cur.fetchone()

        return _build_benco(record)

    def delete_benco(self, bc_id):
        sql = "DELETE FROM benco WHERE bc_id = %s RETURNING *"

        cur = connection.cursor()
        cur.execute(sql, [bc_id])
        connection.commit()
        record = cur.fetchone()
        # Need this to handle raise
        if not record:
            raise ResourceNotFound(f"No record with id {bc_id}")


def _test():
    br = BencoRepo()
    print("--------- ALL BENCOS --------")
    all_bencos = br.all_bencos()
    print(all_bencos)
    # bco = br.get_benco(1)
    # bco.name = "Sarah"
    # bco = br.update_benco(bco)
    # print(bco)

    # test_obj = Benco(name="Grey")
    # br.create_benco(test_obj)
    # TO UPDATE FIRST 'GET' THE OBJECT WITH 'GET' METHOD
    # bco.name = "Dustin"
    # bco = br.update_benco(bco)
    # print(bco)
    # br.delete_benco(4)
    # all_bencos = br.all_bencos()
    # print(all_bencos)


if __name__ == '__main__':
    _test()


import psycopg2
from psycopg2._psycopg import OperationalError
import psycopg2.extras


def create_connection():
    try:
        con = psycopg2.connect(
            host="database-1.cygvfxlspctp.us-east-1.rds.amazonaws.com",
            database="mydb",
            user="postgres",
            password="Qt7fcg3j23TOETfm8JbY",
            port='5432'
        )
        return con
    except OperationalError as e:
        print(f"{e}")
        return None


connection = create_connection()


def _test():
    print(connection)


if __name__ == '__main__':
    _test()

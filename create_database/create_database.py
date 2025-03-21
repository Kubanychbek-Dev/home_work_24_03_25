import os
import pyodbc
from dotenv import load_dotenv
from server_commands import create_database
import connection_str


load_dotenv()


WORK_DATABASE = os.getenv("MS_SQL_DATABASE")
connection_string = connection_str.my_connection()
conn = pyodbc.connect(connection_string)
conn.autocommit = True

if __name__ == "__main__":
    try:
        SQL_QUERY = create_database(WORK_DATABASE)
        conn.execute(SQL_QUERY)
    except pyodbc.ProgrammingError as e:
        print(e)
    except pyodbc.OperationalError as OperErr:
        print(OperErr)
    else:
        print(f"Database {WORK_DATABASE} created")
    finally:
        conn.close()

import os
from dotenv import load_dotenv
import pyodbc
from server_commands import filling_the_database
import connection_str

load_dotenv()

WORK_DATABASE = os.getenv("MS_SQL_DATABASE")
connection_string = connection_str.my_connection()
conn = pyodbc.connect(connection_string)
conn.autocommit = True

cursor = conn.cursor()
table_name = "Tesla"


if __name__ == "__main__":
    try:
        SQL_QUERY = filling_the_database(table_name)
        cursor.execute(fr"USE {WORK_DATABASE}")
        cursor.execute(SQL_QUERY)
    except pyodbc.ProgrammingError as PrErr:
        print(PrErr)
    except pyodbc.IntegrityError as e:
        print(e)
    else:
        print(f"The table '{table_name}' filled")
    finally:
        conn.close()

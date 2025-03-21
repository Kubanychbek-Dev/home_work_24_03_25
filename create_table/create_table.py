import os
from dotenv import load_dotenv
import pyodbc
from server_commands import create_table

load_dotenv()


DRIVER = os.getenv("MS_SQL_DRIVER")
SERVER = os.getenv("MS_SQL_SERVER")
WORK_DATABASE = os.getenv("MS_SQL_DATABASE")
PAD_DATABASE = os.getenv("MS_PAD_DATABASE")
USER = os.getenv("MS_SQL_USER")
PASSWORD = os.getenv("MS_SQL_KEY")

connection_string = f"""DRIVER={DRIVER};
                         SERVER={SERVER};
                          DATABASE={PAD_DATABASE};
                           USER={USER};
                            PASSWORD={PASSWORD};
                            Trusted_connection=yes"""

conn = pyodbc.connect(connection_string)
conn.autocommit = True


cursor = conn.cursor()
table_name = "Tesla"


try:
    SQL_QUERY = create_table(table_name)
    cursor.execute(fr"USE {WORK_DATABASE};")
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ProgErr:
    print(ProgErr)
except pyodbc.Error as e:
    print(e)
else:
    print(f"The table '{table_name}' created")
finally:
    conn.close()

import os
from dotenv import load_dotenv
import pyodbc
from server_commands import create_database

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
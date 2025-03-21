import os
from dotenv import load_dotenv
import pyodbc
from server_commands import get_data_from_database
import connection_str
import json_adapter

load_dotenv()

WORK_DATABASE = os.getenv("MS_SQL_DATABASE")
connection_string = connection_str.my_connection()
conn = pyodbc.connect(connection_string)
conn.autocommit = True

cursor = conn.cursor()
table_name = "Tesla"


dict_list = []


if __name__ == "__main__":
    try:
        SQL_QUERY = get_data_from_database(table_name)
        cursor.execute(fr"USE {WORK_DATABASE}")
        result = cursor.execute(SQL_QUERY)
    except pyodbc.ProgrammingError as pe:
        print(pe)
    except pyodbc.Error as e:
        print(e)
    else:
        records = result.fetchall()
        for record in records:
            data_dict = {"id": record.id,
                         "name": record.Name,
                         "model": record.Model,
                         "price": float(record.Price)
                         }
            dict_list.append(data_dict)
    finally:
        conn.close()


    my_json = json_adapter.JSONAdapter("database.json")
    my_json.to_json(dict_list)

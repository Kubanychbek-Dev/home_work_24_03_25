def create_database(name):
    command = fr"CREATE DATABASE {name}"
    return command


def create_table(name):
    command = fr"""CREATE TABLE {name}
               (id INT PRIMARY KEY,
               Name nvarchar(50),
                Model nvarchar(50),
                 Price money);"""
    return command


def filling_the_database(name):
    command = fr"""INSERT INTO {name}(id, Name, Model, Price)
                   VALUES
                   (1, 'Tesla', 'Model 3', 34900),
                    (2, 'Tesla', 'Models S', 79900),
                     (3, 'Tesla', 'Models Y', 52490),
                      (4, 'Tesla', 'Cybertruck', 69990);"""
    return command


def get_data_from_database(table_name):
    command = fr"""SELECT id, Name, Model, Price
                   FROM {table_name};"""
    return command

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


def inserting_data_to_database(name):
    command = fr"""INSERT INTO {name}(id, Name, Model, Price)
                   VALUES(1,)"""
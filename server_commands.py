def create_database(name):
    command = fr"CREATE DATABASE {name}"
    return command


def create_table(name):
    command = fr"""CREATE TABLE {name}
               (id INT PRIMARY KEY,
               Name nvarchar(50),
                Model nvarchar(50),
                Year date,
                 Price money);"""
    return command
import os
from dotenv import load_dotenv


load_dotenv()

DRIVER = os.getenv("MS_SQL_DRIVER")
SERVER = os.getenv("MS_SQL_SERVER")
# WORK_DATABASE = os.getenv("MS_SQL_DATABASE")
PAD_DATABASE = os.getenv("MS_PAD_DATABASE")
USER = os.getenv("MS_SQL_USER")
PASSWORD = os.getenv("MS_SQL_KEY")


def my_connection():

    connection_string = f"""DRIVER={DRIVER};
                             SERVER={SERVER};
                              DATABASE={PAD_DATABASE};
                               USER={USER};
                                PASSWORD={PASSWORD};
                                Trusted_connection=yes"""
    return connection_string

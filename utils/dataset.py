import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from tqdm import tqdm


load_dotenv()

mysql_settings = {
    "host": os.environ.get("DB_HOST"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME")
}
database_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
    mysql_settings["user"],
    mysql_settings["password"],
    mysql_settings["host"],
    mysql_settings["database"]),  pool_size=20, max_overflow=0)


def get_data(table_name="wines"):
    # read from mysql database and return a pandas dataframe
    conn = database_engine.connect().execution_options(
                stream_results=True)
    with tqdm(desc="Loading data from {}".format(table_name)) as pbar:
        query = text("SELECT * FROM {}".format(table_name))
        df = pd.read_sql(query, conn)
        pbar.update(len(df))
        tqdm._instances.clear()
    return df
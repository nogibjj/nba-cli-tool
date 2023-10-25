"""
This module contains functions to transform and load data into a 
local SQLite3 database. The SQLite3 database is created in the 
current working directory. If the database already exists, it will 
be overwritten.
"""
import sqlite3
import csv
import re


def create_and_load_db(
    dataset: str = "data/GroceryDB_IgFPro.csv",
    db_name: str = "GroceryDB",
    sql_conn: sqlite3.Connection = None,
) -> sqlite3.Connection:
    """ "function to create a local SQLite3 database and load data into it.
    The data is transformed from a CSV file."""

    with open(dataset, newline="") as csvfile:
        payload = list(csv.reader(csvfile, delimiter=","))

    column_names = [name.replace("%", "Perc") if name else "ID" for name in payload[0]]
    # replace the start of the string if its a number
    column_names = [
        f"{name[1:]}{name[0]}" if name[0].isdigit() else name for name in column_names
    ]
    # define a list of characters to replace
    chars_to_replace = [" ", "/", "-", "(", ")", "&", "'", ",", ".", "+", ":", '"']

    # replace each character with an underscore
    for char in chars_to_replace:
        column_names = [name.replace(char, "_") for name in column_names]

    # determine column types
    column_types = []
    for i, value in enumerate(payload[1]):
        if re.match(r"^-?\d+(?:\.\d+)?$", value):
            column_types.append("REAL")
        elif re.match(r"^\d{4}-\d{2}-\d{2}$", value):
            column_types.append("DATE")
        else:
            column_types.append("TEXT")

    if not sql_conn:
        conn = sqlite3.connect(f"{db_name}")
        print(f"Database {db_name} created.")
    else:
        conn = sql_conn

    c = conn.cursor()  # create a cursor
    # drop the table if it exists
    c.execute(f"DROP TABLE IF EXISTS {db_name}")
    print(f"Excuted: DROP TABLE IF EXISTS {db_name}")
    # create the table.
    s = ', '.join([f'{name} {column_types[i]}' for i, name in enumerate(column_names)])
    query = \
    f"CREATE TABLE {db_name} "\
    f"({s})"
    print(f"Excuted: {query}")
    c.execute(query)
    # insert the data
    c.executemany(
        f"INSERT INTO {db_name} VALUES" f"({', '.join(['?']*len(column_names))})",
        payload[1:],
    )

    print(
        f"Excuted: INSERT INTO {db_name} VALUES"
        f"({', '.join(['?']*len(column_names))})"
    )

    conn.commit()
    conn.close()

    return conn


if __name__ == "__main__":
    create_and_load_db()

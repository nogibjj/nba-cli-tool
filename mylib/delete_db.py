"""This module contains functions to delete a table from a local SQLite3 database.""" ""
import sqlite3


def drop_data(
    db_name: str = "GroceryDB.db",
    table_name: str = "GroceryDB",
    sql_conn: sqlite3.Connection = None,
    condition="count_priducts = '11",
) -> None:
    """function to drop data based on condition and table"""
    if not sql_conn:
        conn = sqlite3.connect(db_name)
    else:
        conn = sql_conn

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
    conn.commit()
    conn.close()

    print(f"Table {table_name} dropped from {db_name}.")

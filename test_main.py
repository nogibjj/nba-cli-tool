"""
Test goes here

"""
import sqlite3
import pytest
from mylib.delete_db import drop_data
from mylib.transform_load import create_and_load_db
from mylib.updateDb import update_db
from mylib.query import query
from mylib.extract import extract
import os


@pytest.fixture
def setup_database():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS test_table
                      (id INTEGER PRIMARY KEY,
                       name TEXT,
                       count_products INTEGER)"""
    )
    cursor.execute(
        """INSERT INTO test_table (name, count_products)
                      VALUES ('apple', 10),
                             ('banana', 11),
                             ('orange', 12)"""
    )
    conn.commit()
    yield conn

    conn.close()


def test_drop_data(setup_database):
    drop_data(
        db_name="test.db",
        table_name="test_table",
        condition="count_products = 11",
        sql_conn=setup_database,
    )
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM test_table""")
    rows = cursor.fetchall()
    assert len(rows) == 2
    assert rows[0][1] == "apple"
    assert rows[0][2] == 10
    assert rows[1][1] == "orange"
    assert rows[1][2] == 12

    os.remove("test.db")

    conn.close()


def test_create_and_load_db():
    create_and_load_db(dataset="data/nba_22_23.csv", db_name="test")
    conn = sqlite3.connect("test")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM test""")
    rows = cursor.fetchall()
    assert len(rows) > 1

    os.remove("test")

    conn.close()


def test_update_db(setup_database):
    update_db(
        conn=setup_database,
        query_str="UPDATE test_table SET name = 'Rakeen' WHERE count_products = 11",
    )
    cursor = sqlite3.connect("test.db").cursor()
    cursor.execute("""SELECT * FROM test_table""")
    rows = cursor.fetchall()
    assert rows[1][1] == "Rakeen"
    assert rows[1][2] == 11

    os.remove("test.db")

    setup_database.close()


def test_query(setup_database):
    assert (
        len(query(
            db_name="test.db",
            sql_conn=setup_database,
            query_str="SELECT * FROM test_table WHERE count_products = 11",
        ))
        >= 1
    )

    os.remove("test.db")

    setup_database.close()


def test_extract():
    assert (
        extract(
            url="https://www.basketball-reference.com/leagues/NBA_2023_per_game.html#per_game_stats",
            file_path="data/extract.csv",
        )
        == "data/extract.csv"
    )
    os.remove("data/extract.csv")

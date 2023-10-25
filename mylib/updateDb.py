"""Update the database"""
import sqlite3


def update_db(
    conn: sqlite3.Connection = None, database: str = "GroceryDB", query_str: str = ""
) -> None:
    """Update the database"""
    if not conn:
        conn = sqlite3.connect(database)
        print(f"Database {database} Connected to.")

    cursor = conn.cursor()

    if query_str == "":
        cursor.execute(
            "UPDATE GroceryDB SET semantic_tree_name = 'Rakeen'"
            " WHERE count_products = '11'"
        )
    else:
        cursor.execute(query_str)

    conn.commit()

    print("Records updated")


if __name__ == "__main__":
    conn_ = sqlite3.connect("GroceryDB.db")
    update_db(conn_)
    conn_.close()

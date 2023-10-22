import argparse
from mylib.extract import extract
from mylib.transform_load import create_and_load_db
from mylib.query import query
from mylib.updateDb import update_db
from mylib.delete_db import drop_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some data.")
    parser.add_argument(
        "-e", "--extract", action="store_true", help="Extract data from csv url"
    )
    parser.add_argument(
        "-c", "--load", action="store_true", help="Create DB and Load data"
    )
    parser.add_argument("-q", "--query", action="store_true", help="Query data")
    parser.add_argument("-u", "--update", action="store_true", help="Update data")
    parser.add_argument(
        "-d",
        "--delete",
        action="store_true",
        help="Delete from table based on condition",
    )
    parser.add_argument(
        "-v",
        "--url",
        help="CSV url",
        default="https://www.basketball-reference.com/leagues/NBA_2023_per_game.html#per_game_stats",
    )
    parser.add_argument(
        "-f", "--file", help="File path", default="data/GroceryDB_IgFPro.csv"
    )
    parser.add_argument("-db", "--database", help="Database name", default="GroceryDB")
    parser.add_argument("-t", "--table", help="Table name", default="GroceryDB")
    parser.add_argument(
        "-o",
        "--condition",
        help="Condition for delete",
        default="count_products = '11'",
    )
    parser.add_argument("-p", "--query_str", help="Query string", default="")
    parser.add_argument(
        "-y",
        "--update_str",
        help="Update string",
        default="UPDATE GroceryDB SET semantic_tree_name = 'Rakeen' WHERE '\
        'count_products = '11'",
    )

    args = parser.parse_args()

    if args.extract:
        print("Extracting data...")
        extract(args.url, args.file)

    # Creation
    conn = None
    if args.load:
        print("Creating DB and loading data...")
        conn = create_and_load_db(args.file, args.database)

    # Update
    if args.update:
        print("Updating data...")
        update_db(conn, args.database, args.update_str)

    # Read
    if args.query:
        print("Querying data...")
        if conn:
            query(args.query_str, args.database, conn)
        else:
            query(args.query_str, args.database)

    # Deletion
    if args.delete:
        print("Deleting data...")
        drop_data(args.database, args.table, conn, args.condition)

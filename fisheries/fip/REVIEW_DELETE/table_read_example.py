import argparse
from psycopg2 import sql

from .. import database_connection


def get_first_row_of_table(conn, table_name):
    """Retrieves and returns the first row of the specified table along with column headers."""
    with conn.cursor() as cursor:
        # Create a safe SQL string
        query = sql.SQL("SELECT * FROM {} LIMIT 1").format(sql.Identifier(table_name))
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch the first row
        row = cursor.fetchone()
        
        # Get the column headers
        col_headers = [desc[0] for desc in cursor.description]
        
        return col_headers, row


def main(table_name):
    with database_connection() as conn:
        # Use the get_first_row_of_table function
        headers, first_row = get_first_row_of_table(conn, table_name)
        # Print column headers and first row
        print("Column Headers:", headers)
        print("First Row:", first_row)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Get the first row of a table from a PostGIS database.')
    parser.add_argument('table_name', type=str, help='The name of the table to query.')
    args = parser.parse_args()

    # Call main function with the table name argument
    main(args.table_name)

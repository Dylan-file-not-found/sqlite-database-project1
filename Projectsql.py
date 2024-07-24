import sqlite3

# Provide the correct path to your SQLite database file
db_path = r'C:\Users\Dylan\OneDrive\Escritorio\SqliteDBproject.db'

try:
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example query to fetch all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print the list of tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Example query to fetch all records from a specific table
    table_name = 'United_State'
    cursor.execute(f"SELECT * FROM {table_name};")
    records = cursor.fetchall()

    # Print the fetched records
    print(f"Records in table {table_name}:")
    for record in records:
        print(record)

except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
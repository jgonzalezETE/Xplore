import sqlite3

if __name__ == '__main__':
    pass

table_name = input("Enter table name: ")

# Connect to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("../../master_table.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

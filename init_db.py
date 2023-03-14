import sqlite3

# Open a connection with database file called database.db
connection = sqlite3.connect('database.db')

# Open function will open the schema.sql file as f and executes the SQL file contents using executescript
with open('schema.sql') as f:
    connection.executescript(f.read())

# Create a cursor object that allows the use of the execute() method for the two proceeding SQL statements
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

# Commit the changes and close the connection
connection.commit()
connection.close()
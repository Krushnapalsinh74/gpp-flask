import sqlite3

# Connect to the database
conn = sqlite3.connect('instance/app.db')
cursor = conn.cursor()

# Drop the alembic_version table if it exists
cursor.execute("DROP TABLE IF EXISTS alembic_version")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Migration tracking table dropped successfully")

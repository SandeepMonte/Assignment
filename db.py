import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    location TEXT,
                    gender TEXT
                )''')

# Insert sample data into the users table
sample_data = [
    ('John Doe', 'john@example.com', 'New York', 'male'),
    ('Jane Smith', 'jane@example.com', 'Los Angeles', 'female'),
    ('Alice Johnson', 'alice@example.com', 'Chicago', 'female'),
    # Add more sample data as needed
]

cursor.executemany('INSERT INTO users (name, email, location, gender) VALUES (?, ?, ?, ?)', sample_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Sample data has been inserted into the users table.")

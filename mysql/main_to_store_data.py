import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, values=None):
    """Execute a single query."""
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query):
    """Fetch results from a single query."""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Replace with your own MySQL server and database credentials
connection = create_connection("localhost", "root", "7896", "kddb")

# Example: Creating a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT,
    gender TEXT,
    nationality TEXT
)
"""
execute_query(connection, create_table_query)

# Example: Inserting data into the table
insert_user_query = """
INSERT INTO users (name, age, gender, nationality) VALUES (%s, %s, %s, %s)
"""
user_data = ("Neha", 32, "female", "IND")
execute_query(connection, insert_user_query, user_data)

# Example: Fetching data from the table
select_users_query = "SELECT * FROM users WHERE id = 1"
select_users_query = "SELECT * FROM users"
users = fetch_query(connection, select_users_query)

for user in users:
    print(user)

# Close the connection when done
if connection:
    connection.close()
    print("The connection is closed")


import mysql.connector

# Replace with your actual credentials
host = "localhost"
# host = "localhost:3306"
user = "root"  # Usually 'root' by default
password = "7896"
database = "kddb"

try:
    # Establish a connection to MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Perform operations here (e.g., execute queries, fetch data)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    print("May be your Database is not running or address is wrong")

finally:
    # Close the connection if it is still open
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

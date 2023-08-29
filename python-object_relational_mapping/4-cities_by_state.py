import MySQLdb
import sys


def list_cities(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        # Create the SQL query
        query = "SELECT cities.id, cities.name, states.name FROM states "
        query += "JOIN cities ON  states.id = cities.state_id "
        query += "ORDER BY cities.id ASC"
        cursor.execute(query)
        # Fetch all the results
        results = cursor.fetchall()
        # Display the results
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("must <mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_cities(username, password, database)

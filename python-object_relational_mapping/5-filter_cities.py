import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
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
        # Create the SQL query using user input with parameterized values
        query = "SELECT cities.name FROM cities "
        query += "JOIN states ON states.id = cities.state_id "
        query += "WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))
        # Fetch all the results
        results = cursor.fetchall()
        # Display the results as a comma-separated list
        city_names = [row[0] for row in results]
        print(", ".join(city_names))
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("<mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        list_cities_by_state(username, password, database, state_name)

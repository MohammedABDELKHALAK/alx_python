import MySQLdb
import sys


def list_states_with_n(username, password, db_name):
    try:
        # Connect to the database
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=db_name)
        # Create a cursor
        cursor = db.cursor()
        # Execute the query BINARY to retrieve just upper n
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        query += "ORDER BY id ASC"
        cursor.execute(query)
        # Fetch all the results
        results = cursor.fetchall()
        # Display the results
        for row in results:
            print(row)
        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("<username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states_with_n(username, password, db_name)

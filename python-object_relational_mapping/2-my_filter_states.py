import MySQLdb
import sys


def search_state(username, password, db_name, state_name):
    try:
        # Connect to the database
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=db_name)

        # Create a cursor
        cursor = db.cursor()
        # Execute the query
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        cursor.execute('{}'.format(query), (state_name,))
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
    if len(sys.argv) != 5:
        print("<username> <password> <db_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    search_state(username, password, db_name, state_name)

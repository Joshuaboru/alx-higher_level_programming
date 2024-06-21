<F11>import MySQLdb
import sys

def list_states(username, password, db_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Execute the query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)


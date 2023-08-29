import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database}')
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query the first State object ordered by id
        first_state = session.query(State).order_by(State.id).first()
        # Display the result
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("<mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        print_first_state(username, password, database)

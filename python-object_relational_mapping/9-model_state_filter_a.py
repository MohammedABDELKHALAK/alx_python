import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a(username, password, database):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database}')
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query State objects containing the letter "a" and order by id
        states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
        # Display the results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
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

        filter_states_with_a(username, password, database)

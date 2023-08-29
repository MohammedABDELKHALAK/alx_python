from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the MySQL server
engine = create_engine(
    'mysql://username:password@localhost:3306/database_name')
# Create a declarative base
Base = declarative_base()


class State(Base):
    """
    state class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create the table
    Base.metadata.create_all(engine)
    # Example of using the State class
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='New York')
    session.add(new_state)
    session.commit()
    # Close the session
    session.close()

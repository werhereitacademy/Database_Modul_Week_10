import psycopg2
from db_controllers.config import load_config


def connect(db_name):
    """Connect to the PostgreSQL database server"""
    try:
        config = {**load_config()}
        # connecting to the PostgreSQL server
        with psycopg2.connect(
            database=db_name,
            host=config["host"],
            user=config["user"],
            password=config["password"],
        ) as conn:
            print("Connected to the PostgreSQL server.")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    connect("crm")

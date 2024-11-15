from dotenv import load_dotenv
import os


def load_config(filename=".env"):
    load_dotenv(dotenv_path=filename)

    config = {
        "host": os.getenv("POSTGRESQL_HOST"),
        "database": os.getenv("POSTGRESQL_DATABASE"),
        "user": os.getenv("POSTGRESQL_USER"),
        "password": os.getenv("POSTGRESQL_PASSWORD"),
    }

    if not all(config.values()):
        raise Exception("Some environment variables are missing in the .env file")

    return config


if __name__ == "__main__":
    config = load_config()
    print(config)

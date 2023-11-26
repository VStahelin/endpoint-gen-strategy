import sqlite3
import uuid


def connect_to_database(database_name="test.db"):
    connection = sqlite3.connect(database_name)
    return connection


def create_base_path_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS base_path (
            id INTEGER PRIMARY KEY,
            path TEXT UNIQUE
        )
    """
    )

    connection.commit()


def create_hash_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS hashs (
            id TEXT PRIMARY KEY UNIQUE,
            param TEXT,
            base_path_id INTEGER,
            FOREIGN KEY (base_path_id) REFERENCES base_path (id)
        )
    """
    )

    connection.commit()


def get_or_create_base_path(connection, path):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM base_path WHERE path = ?", (path,))
    existing_path = cursor.fetchone()

    if existing_path:
        return existing_path

    cursor.execute("INSERT INTO base_path (path) VALUES (?)", (path,))
    connection.commit()

    cursor.execute("SELECT * FROM base_path WHERE path = ?", (path,))
    new_path = cursor.fetchone()

    return new_path


def insert_hash(connection, param, base_path_id):
    cursor = connection.cursor()

    hash_id = str(uuid.uuid4())

    success = False
    while not success:
        try:
            cursor.execute(
                "INSERT INTO hashs (id, param, base_path_id) VALUES (?, ?, ?)",
                (hash_id, param, base_path_id),
            )
            connection.commit()

            success = True
            return hash_id

        except sqlite3.IntegrityError as e:
            print(f"Error: {e}. The id '{hash_id}' already exists in the hashs table.")
            hash_id = str(uuid.uuid4())

        finally:
            cursor.close()


def query_base_paths(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM base_path")
    result = cursor.fetchall()

    return result


def query_hashs(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM hashs")
    result = cursor.fetchall()

    return result


def get_hash(connection, hash_id):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM hashs WHERE id = ?", (hash_id,))
    result = cursor.fetchone()

    return result


def close_connection(connection):
    connection.close()

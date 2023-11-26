from db import (
    connect_to_database,
    create_base_path_table,
    create_hash_table,
    insert_hash,
    query_base_paths,
    query_hashs,
    close_connection,
    get_or_create_base_path,
    get_hash,
)

BASE_URL = "https://vitor.com.br"

connection = connect_to_database()


def setup_database():
    create_base_path_table(connection)
    create_hash_table(connection)


def query_tables():
    print("\nQuerying tables:")
    base_paths = query_base_paths(connection)
    hashs = query_hashs(connection)

    print("Base Paths:")
    for row in base_paths:
        print(row)

    print("\nHashs:")
    for row in hashs:
        print(row)


def verify_api_path(api_path: str):
    if api_path.startswith("/"):
        api_path = f"{api_path}"

    return api_path


def create_notification_endpoint(api_path: str, param: str, base_url: str = BASE_URL):
    api_path = verify_api_path(api_path)

    base_path_id = get_or_create_base_path(connection, path=api_path)[0]
    hash_path_id = insert_hash(connection, param=param, base_path_id=base_path_id)
    return f"{base_url}/api/{hash_path_id}"


def get_path(hash_id: str):
    try:
        notification_object = get_hash(connection, hash_id=hash_id)
        return notification_object

    except TypeError:
        print("Hash not found.")
        return None


if __name__ == "__main__":
    setup_database()

    print("======1======")
    api_path = "/v1/pay/notify/"
    param = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum."
    notification_url1 = create_notification_endpoint(
        api_path=api_path,
        param=param,
    )
    hash_id1 = notification_url1.split("/")[-1]
    notification_object1 = get_path(hash_id=hash_id1)

    print(f"API Path: {api_path}, Param: {param}")
    print(f"Notification URL1: {notification_url1}")
    print(f"Notification URL1 Length: {len(notification_url1)}")
    print(f"Hash ID: {hash_id1}")
    print(f"Notification Object: {notification_object1}")

    print("\n======2======")
    api_path = "/v1/payment/notification/webhook/"
    param = "364ddde1-08e3-4ada-90a3-96c1d8dff601"
    notification_url2 = create_notification_endpoint(
        api_path=api_path,
        param=param,
    )
    hash_id2 = notification_url2.split("/")[-1]
    notification_object2 = get_path(hash_id=hash_id2)

    print(f"API Path: {api_path}, Param: {param}")
    print(f"Notification URL2: {notification_url2}")
    print(f"Notification URL2 Length: {len(notification_url2)}")
    print(f"Hash ID: {hash_id2}")
    print(f"Notification Object: {notification_object2}")

    query_tables()

    close_connection(connection)

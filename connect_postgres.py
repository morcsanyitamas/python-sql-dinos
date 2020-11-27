import psycopg2

def connect_to_database(user_name, password, host, database_name):
    try:
        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name)
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        return connection
    except expression as identifier:
        print(exception)

def delete_data(name):
    try:
        connection = connect_to_database("postgres", "tomi", "localhost", "test_db")
        cursor = connection.cursor()
        query_string = "DELETE FROM dinos WHERE dinos.name = %s"
        values = (name)
        cursor.execute(query_string, values)
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if 'connection' in locals():
            connection.close()

def insert_data(name, height, length):
    try:
        connection = connect_to_database("postgres", "tomi", "localhost", "test_db")
        cursor = connection.cursor()
        query_string = "INSERT INTO dinos (name, height, length) VALUES (%s, %s, %s)"
        values = (name, height, length)
        cursor.execute(query_string, values)
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if 'connection' in locals():
            connection.close()

def get_data(query_string):
    try:
        connection = connect_to_database("postgres", "tomi", "localhost", "test_db")
        cursor = connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if 'connection' in locals():
            connection.close()


if __name__ == '__main__':
    main()

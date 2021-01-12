from .model_init import connect_to_DB

connection = connect_to_DB()


def get_all():
    with connection.cursor() as cursor:
        query = "SELECT * FROM Subjects "
        cursor.execute(query)
        result = cursor.fetchall()
        return result



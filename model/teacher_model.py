from .model_init import connect_to_DB

connection = connect_to_DB()


def get_by_subject(subject_id,gender):
    with connection.cursor() as cursor:
        # query = """SELECT * FROM Teachers join SubjectsForTechers on Teachers.id = SubjectsForTechers.teacher_id
        #             WHERE SubjectsForTechers.subject_id ={}""".format(subject_id)
        query = "SELECT DISTINCT  Teachers.*  FROM Teachers join SubjectsForTechers on Teachers.id = SubjectsForTechers.teacher_id WHERE 1=1"
        if subject_id:
            query+=" AND SubjectsForTechers.subject_id ={}".format(subject_id)
        else:
            query += " AND Teachers.gender='{}'".format(gender)
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def get_by_gender(gender):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Teachers WHERE gender {}".format(gender)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

from .model_init import connect_to_DB

connection = connect_to_DB()


def add(first_name, last_name, e_mail, phone, gender,aviable_after_lesson):
    with connection.cursor() as cursor:
        query = """insert into  Teachers(first_name,last_name, e_mail,phone,gender, likes, aviable_after_lesson) 
                values ('{}', '{}', '{}', '{}', '{}', {}, {})""".format(first_name, last_name,  e_mail,phone,gender, '0' , aviable_after_lesson)
        cursor.execute(query)
        connection.commit()
        
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


def get_max_id():
    with connection.cursor() as cursor:
        query = "SELECT max(id) as max_id FROM Teachers"
        cursor.execute(query)
        result = cursor.fetchone()
        print(result['max_id'])
        return result['max_id']

def add_subjects(teacher_id, subjects_id_list):
    with connection.cursor() as cursor:
        for sub_id in subjects_id_list:
            query = "insert into SubjectsForTechers (teacher_id, subject_id) values({},{})".format(teacher_id, sub_id)
            cursor.execute(query)
        connection.commit()



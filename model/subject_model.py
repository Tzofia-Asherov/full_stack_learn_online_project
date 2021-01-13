from .model_init import connect_to_DB

connection = connect_to_DB()


def get_all():
    with connection.cursor() as cursor:
        query = "SELECT * FROM Subjects "
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def get_by_teacher_id(teacher_id):
    with connection.cursor() as cursor:
        query = """select Subjects.description, Subjects.category , subject_id
                    from SubjectsForTechers join Subjects on SubjectsForTechers.subject_id = Subjects.id
                    where SubjectsForTechers.teacher_id = {}""".format(teacher_id)
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def is_teacher_teach_subjects(teacher, all_words):
    subject_list = get_by_teacher_id(teacher['id'])
    if subject_list ==[]:
        return False
    for subject in subject_list:
        for word in all_words:
            if word.lower() in subject["category"].lower() or word in subject["description"].lower():
                return True
    return False



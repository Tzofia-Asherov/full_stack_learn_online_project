from .model_init import connect_to_DB

connection = connect_to_DB()


def add(first_name, last_name, e_mail, phone, gender,aviable_after_lesson):
    with connection.cursor() as cursor:

        #query =  """insert into  Teachers(first_name, last_name, e_mail, phone, gender, likes, aviable_after_lesson) 
        #        values ('{}', '{}', '{}', '{}' '{}', 0, {} )""".format(first_name, last_name, e_mail, phone, gender,aviable_after_lesson)
        query = """insert into  Teachers(first_name,last_name, e_mail,phone,gender, likes, aviable_after_lesson) 
                values ('{}', '{}', '{}', '{}', '{}', {}, {})""".format(first_name, last_name,  e_mail,phone,gender, '0' , aviable_after_lesson)
        cursor.execute(query)
        connection.commit()

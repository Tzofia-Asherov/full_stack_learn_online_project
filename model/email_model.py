from project_utils import email
from .model_init import connect_to_DB

connection = connect_to_DB()


def send_to_teacher(teacher,name, e_mail, phone, content):
    email_content = "hello,\n I am {}.\n {}\n Thanks! \n{} \nphone: {}, mail: {}".format(name,content,name,phone,e_mail)

    with connection.cursor() as cursor:
        query = "SELECT * FROM Teachers where id ={}  ".format(teacher)
        cursor.execute(query)
        result = cursor.fetchone()

    email.send(result.get("e_mail"), email_content)

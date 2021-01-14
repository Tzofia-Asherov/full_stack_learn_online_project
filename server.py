from flask import Flask, render_template, request
from model import teacher_model, subject_model, comments_model, email_model
import utils

import json

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
# 

@app.route('/')
def root():
    subject_lst = subject_model.get_all()
    comment_lst = comments_model.get_all()
    return render_template('index.html', data={"subjects": subject_lst, "teachers": [], "comments": comment_lst})


@app.route('/teachers', methods=["POST"])
def add_teacher():
    teacher_details = request.form
    first_name = teacher_details.get("first_name")
    last_name  = teacher_details.get("last_name")
    e_mail =  teacher_details.get("e_mail")
    phone = teacher_details.get("phone")
    gender = teacher_details.get("gender")
    aviable_after_lesson = teacher_details.get("aviable_after_lesson")
    subjects_id_list =  teacher_details.getlist("teacher_subjects")
   
    if first_name == '' or last_name == '' or e_mail == '' or gender == 'gender':
        return render_template("error_input_teacher.html", data = {"message":"you must have first name, last name, e-mail and gender"})

    phone, aviable_flag = utils.validate_teacher(phone, aviable_after_lesson)
  

    teacher_model.add(first_name, last_name, e_mail, phone, gender, aviable_flag)
    teacher_id =  teacher_model.get_max_id() 
    teacher_model.add_subjects(teacher_id, subjects_id_list)

    subject_lst = subject_model.get_all()

    return render_template("success_page.html",  data={"subjects": subject_lst, "teachers": []})

        

@app.route('/teachers', methods=["GET"])
def get_teachers():
    subject_id = request.args.get("subject")
    search = request.args.get("search")
    gender = request.args.get("gender")
    subject_lst = subject_model.get_all()
    teacher_list = teacher_model.get_all()
    teacher_back = []
    if search == '' or search == None:
       teacher_back = teacher_list
    else:
        word_list = search.split(' ')
        for teacher in teacher_list:
            if subject_model.is_teacher_teach_subjects(teacher, word_list):
                teacher_back.append(teacher)
    
    for teacher in teacher_back:
        if teacher["aviable_after_lesson"] == b"\x01":
            teacher["aviable_after_lesson"] = 'yes'
        else:
            teacher["aviable_after_lesson"] = 'no'

    if gender == 'male' or gender =='female':
        teacher_back = [t for t in teacher_back if t["gender"] == gender]

    return render_template('find_teacher.html', data={"teachers": teacher_back, "subjects": subject_lst })


# @app.route('/teachers', methods=["GET"])
# def get_teachers():
#     subject_id = request.args.get("subject")
#     gender = request.args.get("gender")
#     subject_lst = subject_model.get_all()
#     teacher_lst = teacher_model.get_all()
#     if subject_id is None and gender is None:
#         return render_template('find_teacher.html', data={"teachers": teacher_lst, "subjects": subject_lst })
#     teacher_lst = teacher_model.get_by_subject(subject_id, gender)  
#     return render_template('find_teacher.html', data={"teachers": teacher_lst, "subjects": subject_lst })

@app.route('/teachers/<id_teacher>')
def display_teacher(id_teacher):
    like = request.args.get("like", None)
    if like:
        teacher_model.update_like(id_teacher)

    subject_lst = teacher_model.get_subjects(id_teacher)
    teacher = teacher_model.get_one(id_teacher)[0]
    data={"teacher": teacher, "subjects": subject_lst }
    data['teacher']['aviable_after_lesson']  = False if data['teacher']['aviable_after_lesson'] == b'\x00' else True

    return render_template('display_teacher.html', data={"teacher": teacher, "subjects": subject_lst })

@app.route('/emails', methods=["POST"])
def send_email():
    teacher_id = request.form.get("teacher")
    name = request.form.get("name")
    e_mail = request.form.get("e_mail")
    phone = request.form.get("phone")
    content = request.form.get("content")
    email_model.send_to_teacher(teacher_id, name, e_mail, phone, content)
    return render_template("success_page.html", data={"subjects": [], "teachers": []})


@app.route('/like')
def like():
    #get id, update like and return it
    return str(2)

if __name__ == "__main__":
    app.run(port=3010, debug=True)

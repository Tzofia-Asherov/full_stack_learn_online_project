from flask import Flask, render_template, request
from model import teacher_model, subject_model
import utils

import json

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')
# 

@app.route('/')
def root():
    subject_lst = subject_model.get_all()
    return render_template('index.html', data={"subjects": subject_lst, "teachers": []})    


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
   
    if first_name == '""' or e_mail == '':
        render_template("error.py")

    last_name , phone, aviable_flag = utils.validate_teacher(last_name , phone, aviable_after_lesson)
  

    teacher_model.add(first_name, last_name, e_mail, phone, gender, aviable_flag)
    teacher_id =  teacher_model.get_max_id() 
    teacher_model.add_subjects(teacher_id, subjects_id_list)

    subject_lst = subject_model.get_all()

    return render_template("success_page.html",  data={"subjects": subject_lst, "teachers": []})

        

@app.route('/teachers', methods=["GET"])
def get_teachers():
    subject_id = request.args.get("subject")
    gender = request.args.get("gender")
    subject_lst = subject_model.get_all()
    teacher_lst = teacher_model.get_all()
    if subject_id is None and gender is None:
        return render_template('find_teacher.html', data={"teachers": teacher_lst, "subjects": subject_lst })
    teacher_lst = teacher_model.get_by_subject(subject_id, gender)  
    return render_template('find_teacher.html', data={"teachers": teacher_lst, "subjects": subject_lst })


if __name__ == "__main__":
    app.run(port=3010, debug=True)

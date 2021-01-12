from flask import Flask, render_template, request
from model import teacher_model, subject_model

import json

app = Flask(__name__, static_url_path='', template_folder='template')
# , static_folder='static'

@app.route('/')
def root():
    subject_lst = subject_model.get_all()
    return render_template('index.html', data={"name": "hellooooooooooooo", "subjects": subject_lst, "teachers": []})    


@app.route('/teachers', methods=["POST"])
def add_teacher():
    teacher_details = request.form
    first_name = teacher_details["first_name"]
    last_name  = teacher_details["last_name"]
    e_mail =  teacher_details["e_mail"]
    phone = teacher_details["phone"]
    gender = teacher_details["gender"]
    aviable_after_lesson = teacher_details.get("aviable_after_lesson")
    aviable_flag = False
    if aviable_after_lesson == 'on':
        aviable_flag = True
    #if first_name == None or e_mail == None:
    #     return render_template("register_teacher.html")
    teacher_model.add(first_name, last_name, e_mail, phone, gender, aviable_flag) 
    return render_template("success_page.html")

        

@app.route('/teachers', methods=["GET"])
def get_teachers():
    subject_id = request.args.get("subject")
    gender = request.args.get("gender")
    teacher_lst = teacher_model.get_by_subject(subject_id,gender)
    subject_lst = subject_model.get_all()
    return render_template('pricing.html', data={"teachers": teacher_lst, "subjects": subject_lst })


if __name__ == "__main__":
    app.run(port=3010, debug=True)

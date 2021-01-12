from flask import Flask, render_template, request
from model import subject_model, teacher_model

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')


@app.route('/')
def root():
    subject_lst = subject_model.get_all()
    return render_template('index.html', data={"name": "hellooooooooooooo", "subjects": subject_lst, "teachers": []})


# @app.route('/teachers', methods=["POST"])
# def add_teacher():
#     try:
#
#         return render_template('index.html')
#     except:
    # teacher_details = request.form
    # first_name = teacher_details["first_name"]
    # last_name = teacher_details["last_name"]


@app.route('/teachers', methods=["GET"])
def get_teachers():
    subject_id = request.args.get("subject")
    gender = request.args.get("gender")
    teacher_lst = teacher_model.get_by_subject(subject_id,gender)
    subject_lst = subject_model.get_all()
    return render_template('pricing.html', data={"teachers": teacher_lst, "subjects": subject_lst })


if __name__ == "__main__":
    app.run(port=3010, debug=True)

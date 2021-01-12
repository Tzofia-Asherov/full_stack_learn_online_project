from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')


@app.route('/')
def root():
    return render_template('index.html',t={"name":"hellooooooooooooo"})


# @app.route('/teachers', methods=["POST"])
# def add_teacher():
#     try:
#
#         return render_template('index.html')
#     except:





if __name__ == "__main__":
    app.run(port=3010)

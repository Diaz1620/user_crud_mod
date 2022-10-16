from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/read_all")
def read_all():
    return render_template("read(all).html", all_users = User.retrieve_all())

@app.route('/create_user', methods=['POST'])
def add_user_to_db():
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/")

@app.route('/create_new')
def create_new_user():
    return render_template("create.html")

@app.route('/read_one/<int:id>')
def read_one_page(id):
    data = {
        'id': id
    }
    return render_template("read(one).html", one_user = User.retrieve_one(data))

@app.route('/edit_form/<int:id>')
def editing_form(id):
    data = {
        'id':id
    }
    return render_template("/user_edit.html", that_one_id = User.retrieve_one(data))

@app.route('/users_edit/<int:id>',methods = ['POST'])
def user_edit(id):
    data = {
        "id": id,
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect(f'/read_one/{id}')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/')
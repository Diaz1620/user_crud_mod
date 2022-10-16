from readline import insert_text
from flask_app import app
from flask import render_template, request, redirect
from user import User

@app.route("/")
def index():
    mysql = connectToMySQL('users')	        # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(users)
    return render_template("read(all).html", all_users = users)

@app.route('/create_user', methods=['POST'])
def add_user_to_db():
    mysql = connectToMySQL("users")

    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    new_user_id = mysql.query_db(query,data)
    return redirect("/")

@app.route('/create_new')
def create_new_user():
    return render_template("create.html")

@app.route('/read_one/<int:id>')
def read_one_page(id):
    query = "SELECT first_name, last_name, email, created_at, updated_at FROM users WHERE id = %(id)s"
    data = {
        'id': id
    }
    db = connectToMySQL("users")
    bd = db.query_db(query,data)
    return render_template("read(one).html", one_user = bd)

@app.route('/edit_form/<int:id>')
def editing_form(id):
    query = "SELECT id FROM users WHERE id = %(id)s"
    data = {
        'id':id
    }
    one_person = connectToMySQL('users')
    base = one_person.query_db(query,data)
    return render_template("/user_edit.html", that_one_id = base)

@app.route('/users_edit/<int:id>',methods = ['POST'])
def user_edit(id):
    query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(email)s WHERE id = %(id)s"
    data = {
        "id": id,
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    mysql = connectToMySQL('users')
    mysql.query_db(query,data)
    
    return redirect(f'/read_one/{id}')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        'id': id
    }
    one_person =connectToMySQL('users')
    base = one_person.query_db(query,data)
    return redirect('/')
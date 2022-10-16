from flask_app.config.mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
from flask_app import app
from flask_app.controllers import users


if __name__ == "__main__":
    app.run(debug=True)
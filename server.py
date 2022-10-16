from flask import render_template, request, redirect
from flask_app.config.mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)
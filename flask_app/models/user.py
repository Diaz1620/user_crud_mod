from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.fname = data['first_name']
        self.lname = data['last_name']
        self.email = data["email"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def retrieve_all(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL('users').query_db(query)
        users = []
        for user in users_from_db:
            users.append(cls(user))
        return users

    @classmethod
    def retrieve_one(cls,data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        user_from_db = connectToMySQL('users').query_db(query, data)

        return cls(user_from_db[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users').query_db(query, data)


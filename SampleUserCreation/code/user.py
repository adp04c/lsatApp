import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(query, (username,)) # finding the user, must use a tuple for the parameter passed into the sql query
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[3])
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(query, (id,)) # finding the user, must use a tuple for the parameter passed into the sql query
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[3])
        else:
            user = None
        
        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.requestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = 'This field is required'
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = 'This field is required.')
        
    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
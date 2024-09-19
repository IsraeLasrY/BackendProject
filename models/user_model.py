from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app

class UserModel:
    def __init__(self):
        self.collection = app.mongo.db.users

    def create_user(self, username, password):
        hashed_password = generate_password_hash(password)
        user = {'username': username, 'password': hashed_password}
        return self.collection.insert_one(user)

    def find_by_username(self, username):
        return self.collection.find_one({'username': username})

    def check_password(self, user, password):
        return check_password_hash(user['password'], password)

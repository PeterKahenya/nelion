import hashlib
import os
from mongoengine import document,fields,connect

MONGO_DB_NAME = 'nelion'
url="mongodb://172.24.0.3:27017/"+MONGO_DB_NAME
connect(host=url)

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storage = salt + key
    return storage

def verify_password(password_to_check,correct_password):
    correct_salt = correct_password[:32]
    correct_key = correct_password[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', password_to_check.encode('utf-8'), correct_salt, 100000)
    return new_key == correct_key


class User(document.Document):
    meta = {'collection':'users'}
    first_name = fields.StringField(max_length=255,required=False)
    last_name = fields.StringField(max_length=255,required=False)
    email = fields.EmailField(required=True,unique=True)
    password = fields.BinaryField(required=True)

    def set_password(self,password):
        self.password = hash_password(password)

    def check_password(self,password_to_check):
        return verify_password(password_to_check,self.password)

users = User.objects
print(users)
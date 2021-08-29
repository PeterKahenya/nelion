import hashlib
import os

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


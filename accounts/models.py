from mongoengine import document,fields
from accounts import hash_password,verify_password


class User(document.Document):
    meta = {'collection':'users'}
    first_name = fields.StringField(max_length=255,required=False)
    last_name = fields.StringField(max_length=255,required=False)
    email = fields.EmailField(required=True,unique=True)
    password = fields.BinaryField(required=True)

    def data(self):
        d = {
            "first_name":str(self.first_name),
            "last_name":str(self.last_name),
            "email":str(self.email),
        }
        return d


    def set_password(self,password):
        self.password = hash_password(password)

    def check_password(self,password_to_check):
        return verify_password(password_to_check,self.password)


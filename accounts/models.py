from mongoengine import document, fields
from accounts import hash_password, verify_password


PERMISSIONS = ('Add', 'View', 'Edit', 'Delete')


class Permission(document.Document):
    meta = {'collection': 'permissions'}
    name = fields.StringField(max_length=255)
    object = fields.GenericReferenceField()
    codename = fields.StringField(max_length=10, choices=PERMISSIONS)


class Group(document.Document):
    meta = {'collection': 'groups'}
    name = fields.StringField(max_length=150)
    permissions = fields.ListField(fields.ReferenceField(Permission))


class User(document.Document):
    meta = {'collection': 'users'}
    first_name = fields.StringField(max_length=255, required=False)
    last_name = fields.StringField(max_length=255, required=False)
    email = fields.EmailField(required=True, unique=True)
    password = fields.BinaryField(required=True)
    groups = fields.ListField(fields.ReferenceField(Group))
    permissions = fields.ListField(fields.ReferenceField(Permission))
    is_active = fields.BooleanField()
    is_staff = fields.BooleanField()
    is_superuser = fields.BooleanField()
    joined_on = fields.DateTimeField()
    last_login = fields.DateTimeField()

    def data(self):
        d = {
            "id":str(self.id),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "email": str(self.email),
        }
        return d

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password_to_check):
        return verify_password(password_to_check, self.password)

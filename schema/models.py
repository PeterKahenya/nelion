from django.db import models
from mongoengine import document,fields as f

FIELD_TYPES = ("String","Integer","Float")

class Field(document.Document):
    meta = {'collection':'fields'}
    name = f.StringField(max_length=1000,unique=True)
    user_friendly_name = f.StringField(max_length=1000,unique=True)
    description = f.StringField(max_length=1000,unique=True)
    type = f.StringField(max_length=100, choices=FIELD_TYPES)

class Entity(document.Document):
    meta = {'collection':'entities'}
    collection_name = f.StringField(max_length=1000,unique=True)
    user_friendly_name = f.StringField(max_length=1000)
    description = f.StringField(description=1000)
    fields = f.ListField(f.ReferenceField(Field))
    subentities = f.ListField(f.ReferenceField('self'))
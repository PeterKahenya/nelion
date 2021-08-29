# from mongoengine import document,fields,connect
# from accounts.models import User,Group,Permission,PERMISSIONS
# from schema.models import Field,Entity,FIELD_TYPES
# import bson


# a,r,u,d = PERMISSIONS
# MONGO_DB_NAME = 'nelion'
# url="mongodb://172.24.0.3:27017/"+MONGO_DB_NAME
# connect(host=url)

# f = Field()
# f.name = "first_name"
# f.user_friendly_name = "First Name"
# f.description = "This is the customer's first name"
# f.type = FIELD_TYPES[0]
# f.save()


# s = Entity()
# s.collection_name = "sales"
# s.user_friendly_name = "Sales"
# s.description = "Sales for a customer"
# s.save()


# f = Field.objects.get(id = bson.ObjectId('612ba833cfc64fe86ec4f41b'))
# s = Entity.objects.get(id = bson.ObjectId('612ba854c4a19e8b80109dd5'))


# c = Entity()
# c.collection_name = "customers"
# c.user_friendly_name = "Customers"
# c.description = "List of Customers"
# c.fields.append(f)
# c.collection_name = "customers"
# c.subentities.append(s)
# c.save()

# c = Entity.objects.get(id = bson.ObjectId('612bac26b92807d6f05ac160'))


# p = Permission()
# p.name = "Can View Customers"
# p.object = c
# p.codename = r
# p.save()

# p = Permission.objects.get(id = bson.ObjectId("612bad7c430d20fa251c2b1e"))

# g = Group()
# g.name = "Agents"
# g.permissions.append(p)
# g.save()

# g = Group.objects.get(id = bson.ObjectId("612bb079d5a2a6cd7d4767af"))


# u = User()
# u.first_name = "Peter"
# u.last_name = "Kahenya"
# u.email = "peter.kahenya@nelion12.com"
# u.set_password("1234")
# u.permissions.append(p)
# u.groups.append(g)
# u.save()
from django.shortcuts import render
from mongoengine.errors import NotUniqueError
from rest_framework import views
from .models import User
from rest_framework.response import Response
from django.utils.html import strip_tags

# API Views
class UsersListView(views.APIView):
    
    def get(self,request,format=None):
        users = User.objects
        users_dict = [user.data() for user in users]
        return Response(users_dict)

    def post(self,request,format=None):
        try:
            first_name=strip_tags(request.data["first_name"])
            last_name=strip_tags(request.data["last_name"])
            email=strip_tags(request.data["email"])
            password=strip_tags(request.data["password"])
            u=User()
            u.first_name = first_name
            u.first_name = last_name
            u.email = email
            u.set_password(password)
            u.save()
        except NotUniqueError as e:
            return Response({"error":str(e)},status=400)
        except:
            return Response(status=400)


class UserDetailsView(views.APIView):
    def get(self,request,id=None,format=None):
        if not id:
            return Response({"error":"No id supplied"},status=400)
        try:
            user=User.objects(id=id)[0]
            data=user.data()
        except:
            return Response({"error":"User with ID {} does not exist".format(id)},status=404)
        return Response({"user":data})
    def put(self,request,id=None,format=None):
        pass
    def delete(self,request,id=None,format=None):
        pass


class GroupsListView(views.APIView):
    pass

class GroupDetailView(views.APIView):
    pass

class PermissionsListView(views.APIView):
    pass

class PermissionDetailView(views.APIView):
    pass
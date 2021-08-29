from django.shortcuts import render
from rest_framework import views


class FieldsListView(views.APIView):
    def get(self,request,format=None):
        pass
    def post(self,request,format=None):
        pass

class FieldDetailView(views.APIView):
    def get(self,request,id=None,format=None):
        pass
    def put(self,request,id=None,format=None):
        pass
    def delete(self,request,id=None,format=None):
        pass

class EntitiesListView(views.APIView):
    def get(self,request,format=None):
        pass
    def post(self,request,format=None):
        pass

class EntityDetailView(views.APIView):
    def get(self,request,id=None,format=None):
        pass
    def put(self,request,id=None,format=None):
        pass
    def delete(self,request,id=None,format=None):
        pass
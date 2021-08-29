from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from schema.models import Entity

class DataView(views.APIView):
    def get(self,request,entity=None,format=None):
        if not id:
            return Response({"error":"No id supplied"},status=400)
        try:
            entity=Entity.objects.get(id=entity)
            data=entity.collection_name
        except:
            return Response({"error":"User with ID {} does not exist".format(id)},status=404)
        return Response({"data":data})

    def post(self,request,id=None,format=None):
        pass

    def put(self,request,id=None,format=None):
        pass

    def delete(self,request,id=None,format=None):
        pass

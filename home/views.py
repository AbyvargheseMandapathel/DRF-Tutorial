from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PeopleSerializer
from .models import Person
# Create your views here.

@api_view(['GET'])
def index(request):
    json_response = {
            'course_name':'python',
            'learn': ['flask','django','fastapi'],
            'course_provider': 'scalar'
               }
    return Response(json_response)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color_id__isnull=False)
        serializer = PeopleSerializer(objs , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PUT":
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data = data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted successfully"})
        
    


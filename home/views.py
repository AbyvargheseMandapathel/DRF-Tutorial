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

@api_view(['GET','POST'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        
        serializer = PeopleSerializer(objs , many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    


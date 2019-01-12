from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializer
# Create your views here.

class employeeList(APIView):
    
    def get(self, request):
        employees1=employees.objects.all()
        serializer=employeeSerializer(employees1, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        print (request.data)
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   ''' def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
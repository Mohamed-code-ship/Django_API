from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class FirstView(APIView):
    def get (self, request, *args, **kwargs):
        data ={
            'name':'Moha',
            'nationality':'Kenya',
            'age': 22
        }
        return Response(data)

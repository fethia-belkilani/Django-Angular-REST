from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView

class IndexView(APIView):
   
    def get(self, request, format=None):
        content = {
            'wmsg':'welcome to fullstack dev'
            }
        return Response(content)

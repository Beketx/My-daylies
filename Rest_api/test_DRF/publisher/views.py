from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from publisher.models import Author,Book
from publisher.serializers import AuthorSerializer
# Create your views here.

class AuthorView(APIView):
    def get(self,request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author,many=True)
        return Response({"authors":serializer.data})

    def post(self,request):
        request_body = request.data
        serializer = AuthorSerializer(data=request_body)
        if serializer.is_valid():
            save_author = serializer.save()
        return Response({"success":serializer.data})
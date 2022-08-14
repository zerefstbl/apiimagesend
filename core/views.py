from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PhotoSerializer
from .models import Photo

class PhotoListCreateView(APIView):
  name = 'photo_list_create_view'
  
  def get(self, request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = PhotoSerializer(data=request.data)
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
  
class PhotoEditDeleteView(APIView):
  name = 'photo_edit_delete_view'
  
  def put(self, requst):
    pass

  
  def delete(self, request):
    pass

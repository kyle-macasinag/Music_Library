from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from .serializers import MusicSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(["GET", "POST"])
def music_list(request):

    if request.method == "GET":
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Tracks
from .serializers import TrackSerializer
from .forms import TracksForm

# Web-based Views (HTML Rendering)
def tracks_list(request):
    tracks = Tracks.objects.filter(status=True)
    return render(request, 'tracks/tracks_list.html', {'tracks': tracks})

def add_track(request):
    if request.method == 'POST':
        form = TracksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tracks_list')
    else:
        form = TracksForm()
    return render(request, 'tracks/add_track.html', {'form': form})

def update_track(request, id):
    track = get_object_or_404(Tracks, id=id)
    if request.method == "POST":
        form = TracksForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            form.save()
            return redirect('tracks_list')
    else:
        form = TracksForm(instance=track)
    return render(request, "tracks/add_track.html", {'form': form, 'track': track})

def delete_track(request, id):
    track = get_object_or_404(Tracks, id=id)
    track.status = False
    track.save()
    return redirect('tracks_list')

# API Views
@api_view(['GET'])
def tracks_list_api(request):
    tracks = Tracks.objects.filter(status=True)
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def update_track_api(request, id):
    track = get_object_or_404(Tracks, id=id)

    if request.method == 'GET':  
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    elif request.method == 'PUT':  
        serializer = TrackSerializer(track, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.viewsets import ModelViewSet
from .models import Tracks
from .serializers import TrackSerializer

class TrackViewSet(ModelViewSet):
    queryset = Tracks.objects.filter(status=True) 
    serializer_class = TrackSerializer

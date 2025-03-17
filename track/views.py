from django.shortcuts import render, redirect
from . models import Tracks


def tracks_list(request):
    tracks = Tracks.objects.filter(status=True)
    return render(request, 'tracks/tracks_list.html', {'tracks': tracks})


from . forms import TracksForm
def add_track(request):
    if request.method == 'GET':
        form = TracksForm()
        return render(request, 'tracks/add_track.html', {'form': form})
    else:
        form = TracksForm(request.POST, request.FILES)
        # print(form.data)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('tracks_list')
    return render(request, "tracks/add_track.html", {"form":form})



def update_track(request, id):
    track = Tracks.objects.get(id=id)  
    
    if request.method == "POST":
        form = TracksForm(request.POST, request.FILES, instance=track)  
        if form.is_valid():
            form.save()  
            return redirect('tracks_list') 
    else:
        form = TracksForm(instance=track)  

    return render(request, "tracks/add_track.html", {'form': form, 'track': track})




# create view for delete
def delete_track(request, id):
    track = Tracks.objects.get(id=id)
    track.status = False
    track.save()
    return redirect('tracks_list')

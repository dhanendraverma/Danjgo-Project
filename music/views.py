from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
	all_albums = Album.objects.all()	
	context = {
		'all_albums' : all_albums,
	}
	return render(request, 'music/index.html', {'all_albums':all_albums})


def detail(request,album_id):
	try:
		album = Album.objects.filter(id=album_id).get()
	except:	
		raise Http404("Album doesn't exist")
	return render(request, 'music/details.html', {'album':album})
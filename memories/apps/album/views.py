from django.shortcuts import render
from django.views import generic
from .models import Album
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AlbumListView(generic.ListView):
    model = Album

@method_decorator(login_required, name='dispatch')
class AlbumDetailView(generic.DetailView):
    model = Album

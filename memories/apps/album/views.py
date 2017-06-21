from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AlbumListView(generic.ListView):
    model = Album

    def get_queryset(self):
        return Album.objects.filter(user_id=self.request.user.id)

@method_decorator(login_required, name='dispatch')
class AlbumDetailView(generic.DetailView):
    model = Album

@method_decorator(login_required, name='dispatch')
class AlbumCreate(CreateView):
    model = Album
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['name', 'description']

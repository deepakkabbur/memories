from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

class AlbumListView(LoginRequiredMixin, generic.ListView):
    model = Album

    def get_queryset(self):
        return Album.objects.filter(user_id=self.request.user.id)

class AlbumDetailView(LoginRequiredMixin, generic.DetailView):
    model = Album

class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']

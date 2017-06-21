from django.conf.urls import url
from memories.apps.album import views

urlpatterns = [
    url(r'^albums/$', views.AlbumListView.as_view(), name='albums_list'),
    url(r'^album/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^album/create/$', views.AlbumCreate.as_view(), name='album_create'),
    url(r'^album/(?P<pk>\d+)/update/$', views.AlbumUpdate.as_view(), name='album_update'),
]

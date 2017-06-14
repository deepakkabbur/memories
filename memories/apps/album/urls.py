from django.conf.urls import url
from memories.apps.album import views

urlpatterns = [
    # url(r'^$', views.list, name='index'),
    url(r'^albums/$', views.AlbumListView.as_view(), name='albums_list'),
    url(r'^album/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail')
]

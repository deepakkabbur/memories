from django.conf.urls import url
from memories.core import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup')
]

from django.conf.urls import url
from . import views

app_name = 'bathrooms'
urlpatterns = [
    url(r'^$', views.list, name='list'),
	url(r'^(?P<bathroom_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<bathroom_id>[0-9]+)/vote$', views.vote, name='vote'),
]
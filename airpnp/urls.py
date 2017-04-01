from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'airpnp'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^bathrooms/', include('bathrooms.urls')),
    url(r'^admin/', admin.site.urls),
]
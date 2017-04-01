from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^bathrooms/', include('bathrooms.urls')),
    url(r'^admin/', admin.site.urls),
]
from django.contrib import admin

from .models import Bathroom
from .models import Rating

admin.site.register(Bathroom)
admin.site.register(Rating)

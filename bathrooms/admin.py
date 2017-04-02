from django.contrib import admin

from .models import Location
from .models import Bathroom
from .models import Rating
from .models import Image

admin.site.register(Location)
admin.site.register(Bathroom)
admin.site.register(Rating)
admin.site.register(Image)
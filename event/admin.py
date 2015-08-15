from django.contrib import admin

from .models import *
from promotion.models import Promotion


admin.site.register(Sport)
admin.site.register(Showtime)
admin.site.register(EventOrganizer)
admin.site.register(Movie)
admin.site.register(Concert)
admin.site.register(EventRating)
admin.site.register(PositionPrice)
admin.site.register(GalleryPhoto)
admin.site.register(Promotion)

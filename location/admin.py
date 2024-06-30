from django.contrib import admin

from location.models import LongitudeModel, LatitudeModel, EventModel

admin.site.register(LongitudeModel)
admin.site.register(LatitudeModel)
admin.site.register(EventModel)

from django.contrib import admin
from event.models import Event, PositionPrice
from .models import RecoveryRequests, CustomUser


class PositionInline(admin.StackedInline):
    model = PositionPrice


class EventAdmin(admin.ModelAdmin):
    inlines = [
        PositionInline
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(RecoveryRequests)
admin.site.register(CustomUser)

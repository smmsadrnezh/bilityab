from django.contrib import admin
from .models import RecoveryRequests
from event.models import Event, PositionPrice


class PositionInline(admin.StackedInline):
    model = PositionPrice


class EventAdmin(admin.ModelAdmin):
    inlines = [
        PositionInline
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(RecoveryRequests)


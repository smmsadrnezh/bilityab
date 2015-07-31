from django.contrib import admin

from event.models import Event, PositionPrice


class PositionInline(admin.StackedInline):
    model = PositionPrice


class EventAdmin(admin.ModelAdmin):
    inlines = [
        PositionInline
    ]


admin.site.register(Event, EventAdmin)



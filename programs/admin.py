from .models import Event
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('id', 'title', 'date', 'location', 'posted_by')


admin.site.register(Event, EventAdmin)
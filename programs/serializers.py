from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()


    class Meta:
        model = Event
        fields = ['id', 'posted_by', 'poster', 'title', 'date', 'time_start', 'time_end', 'short_description', 'description', 'location', 'maps_link', 'event_link']

        read_only_fields = ['id']

    
    def get_posted_by(self, obj):
        return obj.posted_by.username if obj.posted_by else None

    
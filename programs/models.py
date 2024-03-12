import uuid
from django.db import models
from users.models import User


class Event(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    maps_link = models.CharField(max_length=255, blank=True, null=True)
    event_link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4())[:15]
        super().save(*args, **kwargs)


    class Meta:
        ordering = ('-created_at',)
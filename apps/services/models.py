from django.db import models
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()
    service_showing_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Service {self.title}'

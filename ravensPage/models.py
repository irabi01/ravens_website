from django.db import models
from datetime import datetime

# Create your models here.
class Events(models.Model):
    heading = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)
    class Meta:
        verbose_name_plural = "Events"
    def __str__(self):
        return self.heading

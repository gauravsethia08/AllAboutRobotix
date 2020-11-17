from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    contact_no = models.CharField(max_length=15)
    message = models.TextField(blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

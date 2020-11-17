from django.db import models
from django.utils import timezone

# Create your models here.
class techspresso(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    abstract = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    pdf_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class iros2020(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    abstract = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    pdf_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class research(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    abstract = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    pdf_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

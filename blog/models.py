from django.db import models

# Create your models here.
class techspresso(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    img = models.ImageField(upload_to = 'pics')
    md_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class iros2020(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    img = models.ImageField(upload_to = 'pics')
    md_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class research(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    img = models.ImageField(upload_to = 'pics')
    md_file = models.FileField(upload_to = 'blog_file')
    blog_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

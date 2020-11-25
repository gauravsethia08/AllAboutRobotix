from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    abstract = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    content = models.TextField()
    blog_type = models.CharField(max_length = 200, choices=[('IROS2020', 'IROS2020'), ('Research', 'Research'), ('Techspresso', 'Techspresso')])
    date_posted = models.DateTimeField(default=timezone.now)
    make_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
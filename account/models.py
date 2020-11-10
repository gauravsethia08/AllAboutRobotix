from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django import forms

# Create your models here.
class studentsManager(BaseUserManager):

  def _create_user(self, email, password, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user



class students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=16, blank=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    num_course_enrolled = models.IntegerField(default=0)
    num_course_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.email
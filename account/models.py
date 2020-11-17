from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, name, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now,
        name = name, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, name, **extra_fields):
    return self._create_user(email, password, False, False, name, **extra_fields)

  def create_superuser(self, email, password, name, **extra_fields):
    user=self._create_user(email, password, True, True, name, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=254, unique=True)
  name = models.CharField(max_length=254, null=True, blank=True, default='')
  institution = models.CharField(max_length=50, default='None')
  github = models.CharField(max_length=50, default='None')
  address = models.CharField(max_length=200, default='None')
  city = models.CharField(max_length=20, default='None')
  country = models.CharField(max_length=30, default='None')
  profile_img = models.ImageField(upload_to = 'pics')
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  last_login = models.DateTimeField(null=True, blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  num_course_taken = models.IntegerField(default=0)
  num_course_completed = models.IntegerField(default=0)

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  objects = UserManager()

  def get_absolute_url(self):
      return "/users/%i/" % (self.pk)


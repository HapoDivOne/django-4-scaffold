from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.shortcuts import get_object_or_404
from users.managers import UserManager
from django.utils import timezone

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
       self.is_deleted = True
       self.save()  

# Create your models here.
class User(AbstractBaseUser, SoftDeleteModel):
  username = None
  last_login = None
  is_staff = None
  is_superuser = None
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  firstname = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255, null=True)
  phone_number = models.CharField(max_length=20, null=True)
  email = models.CharField(max_length=254)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  updated_at = models.DateTimeField(editable=False, null=True)
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = []
  
  objects = UserManager()
  
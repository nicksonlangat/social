from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have email address")
        user    =   self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def search(self):
        return self.get_queryset().search(query=query)

        
    def create_superuser(self, email, password):
        user    =   self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email       =   models.EmailField(verbose_name="email", max_length=100, unique=True)
    username    =   models.CharField(max_length=30, blank=True)
    profile_pic =   models.ImageField(default='default_img/profile.jpeg',
                        upload_to="users/%Y/%m/%d", blank=True, null=True)
    is_admin    =   models.BooleanField(default=False)
    is_active   =   models.BooleanField(default=True) 
    is_staff    =   models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    date_joined =   models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login  =   models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'

    objects =  UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

from django.contrib import admin

admin.site.register(User)
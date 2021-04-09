from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, instagram, tiktok, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            instagram=instagram,
            tiktok=tiktok
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, instagram, tiktok, password):
        user = self.create_user(
            email=email,
            instagram=instagram,
            tiktok=tiktok,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    #username = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=20, null=True, unique=True)
    tiktok = models.CharField(max_length=20, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['instagram','tiktok']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin










#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=30, blank=True, null=True)
#     instagram = models.CharField(max_length=20,blank=True,null=True)
#     tiktok = models.CharField(max_length=20,blank=True,null=True)
#
#     def __str__(self):
#         return str(self.user)
#
#

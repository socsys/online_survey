from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, password=None):
        if not nickname:
            raise ValueError('The Nickname field must be set')

        user = self.model(nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password):
        user = self.create_user(nickname, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    nickname = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'nickname'

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

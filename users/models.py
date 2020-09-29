from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Введите email')
        user = self.model(email=email, **kwargs)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True,
                          **kwargs)
        user.save()
        return user


class User(AbstractUser):
    ROLE = [
        ('USER', 'user'),
        ('ADMIN', 'admin'),
        ('MODERATOR', 'moderator'),
    ]
    role = models.CharField(max_length=9, choices=ROLE, default='user')
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    username = models.CharField(_('username'),
                                max_length=250, blank=True,
                                null=True, unique=True)
    bio = models.CharField(_('bio'), max_length=250, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

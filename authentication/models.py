from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    age = models.PositiveIntegerField(default=16)
    email = models.EmailField(verbose_name='Почта', max_length=255, blank=False)
    image = models.ImageField(upload_to='user/profile')
    position = models.CharField(max_length=255, blank=False)
    telegram = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name, self.last_name

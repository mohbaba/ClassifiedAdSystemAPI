from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.date_registered}"

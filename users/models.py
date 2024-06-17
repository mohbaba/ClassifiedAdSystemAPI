from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    date_registered = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.date_registered}"

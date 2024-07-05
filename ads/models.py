from django.db import models
from users.models import User


# Create your models here.
class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='ads/images/', null=True, blank=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    Category = [('ELECTRONIC', 'Electronic'), ('REAL_ESTATE', 'Real Estate'), ('FASHION', 'Fashion')]
    category = models.CharField(max_length=20, choices=Category)


    def __str__(self):
        return self.title

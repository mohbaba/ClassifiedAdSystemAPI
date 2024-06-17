from django.db import models

from ads.models import Ad
from users.models import User


# Create your models here.
class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time_of_comment = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.commenter} on {self.time_of_comment}'
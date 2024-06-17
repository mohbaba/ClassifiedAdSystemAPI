from django.db import models
from users.models import User
from ads.models import Ad


# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.time_sent}'

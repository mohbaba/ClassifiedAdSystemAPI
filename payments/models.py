from django.db import models

from ads.models import Ad
from users.models import User


# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=100)
    amount = models.FloatField()
    PaymentStatus = [('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed'),
                     ('CANCELLED', 'Cancelled')]
    status = models.CharField(max_length=50, choices=PaymentStatus)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_made')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_received')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_id

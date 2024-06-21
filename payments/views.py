# views.py

from django.shortcuts import render
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction


def initialize_payment(request):
    paystack = Paystack(secret_key='sk_test_cef58d6f6decf4e073b7ed15b014cfcc493f17cb')
    response = Transaction.initialize(reference='unique-reference', amount='amount-in-kobo', email='customer-email')
    data = response['data']
    authorization_url = data['authorization_url']
    return render(request, 'payment.html', {'authorization_url': authorization_url})

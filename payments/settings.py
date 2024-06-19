import json

with open('path/to/secret.json') as f:
    secrets = json.load(f)

PAYSTACK_PUBLIC_KEY = secrets['PAYSTACK_PUBLIC_KEY']
PAYSTACK_SECRET_KEY = secrets['PAYSTACK_SECRET_KEY']

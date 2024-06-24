**Classified Ad System with Paystack API using Django**
===========================================================

**Overview**
------------

This project is a classified ad system built with Python using the Django framework. The system allows users to create, view, and pay for classified ads using the Paystack API for payment processing.

**Features**
------------

* User registration and login system
* Classified ad creation with title, description, price, and image upload
* Ad listing page with pagination and search functionality
* Ad detail page with payment option using Paystack API
* Payment verification and ad activation upon successful payment
* Admin dashboard for managing ads and users

**Technical Requirements**
-------------------------

* Python 3.9+
* Django 3.2+
* Paystack API credentials (available at [Paystack website](https://paystack.com))
* Database: SQLite (default) or any other database supported by Django

**Setup and Installation**
-------------------------

1. Clone the repository: `git clone https://github.com/your-username/classified-ad-system.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a new Paystack API credentials and update the `PAYSTACK_SECRET_KEY` and `PAYSTACK_PUBLIC_KEY` variables in the `settings.py` file
4. Run migrations: `python manage.py migrate`
5. Create a superuser account: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

**Configuration**
---------------

The following configuration options are available:

* `PAYSTACK_SECRET_KEY`: Paystack API secret key
* `PAYSTACK_PUBLIC_KEY`: Paystack API public key
* `PAYSTACK_CALLBACK_URL`: Callback URL for payment verification
* `AD_PRICE`: Default price for classified ads

**Database Schema**
-----------------

The following models are used in the system:

* `User`: User model with fields for username, email, and password
* `Ad`: Classified ad model with fields for title, description, price, image, and user
* `Payment`: Payment model with fields for ad, user, amount, and payment status

**Payment Flow**
--------------

1. User creates a classified ad and selects the payment option
2. System redirects user to Paystack payment gateway
3. User enters payment details and submits payment
4. Paystack API verifies payment and sends callback to system
5. System updates payment status and activates ad if payment is successful

**TODO**
-----

* Implement ad expiration and automatic deactivation
* Add ad reporting and deletion functionality
* Improve search functionality with advanced filtering options
* Implement user rating and review system

**License**
---------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

**Contributing**
---------------

Contributions are welcome! Please submit a pull request or create an issue if you find any bugs or have suggestions for improvement.

**Acknowledgments**
----------------

* Paystack API documentation: [Paystack API Docs](https://paystack.com/docs/api)
* Django documentation: [Django Docs](https://docs.djangoproject.com/en/3.2/)

from django.urls import path

from messaging.views import send_message, get_messages, test_view

urlpatterns = [
    path("send_message", send_message),
    path("viewMessages/<str:sender_phone>/<str:receiver_phone>/", test_view)
]
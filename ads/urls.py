from django.urls import path
from .views import post_ad

urlpatterns = [
    path('postAd/', post_ad),
]
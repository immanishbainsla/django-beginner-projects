from django.urls import path
from urlapp.views import appurlinfo

urlpatterns = [
    path('test/', appurlinfo),
]

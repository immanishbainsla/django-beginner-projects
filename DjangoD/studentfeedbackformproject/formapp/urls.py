from django.urls import path
from formapp.views import feedbackview

urlpatterns = [
    path('', feedbackview),
]

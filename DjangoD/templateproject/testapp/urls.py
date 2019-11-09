from django.urls import path
from testapp.views import wish

urlpatterns = [
    path('wish/', wish)
]

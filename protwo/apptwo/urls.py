from django.conf.urls import url
from apptwo import views

urlpatterns = [
    url(r'^$',views.user,name='user'),
]

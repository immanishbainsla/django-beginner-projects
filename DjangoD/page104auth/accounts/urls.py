from django.urls import path

from accounts.views import signupview
 # ,logout_view
# Urls goes here

app_name = 'accounts'

urlpatterns = [
    path('signup/', signupview, name='signup'),
    # path('logout/', logout_view, name='logout'),
]

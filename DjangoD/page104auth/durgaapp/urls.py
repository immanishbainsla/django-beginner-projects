from django.urls import path

from durgaapp import views

# views goes here

app_name = 'accounts'

urlpatterns = [
    path('java/', views.java_exams_view, name='java'),
    path('python/', views.python_exams_view, name='python'),
    path('aptitude/', views.aptitude_exams_view, name='aptitude'),
]

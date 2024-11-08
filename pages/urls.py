from django.urls import path
from . import views


urlpatterns=[
    path("" , views.Home.as_view() , name = 'home'),
    path('signup/' , views.SignupView.as_view() ,  name = 'signup'),
]
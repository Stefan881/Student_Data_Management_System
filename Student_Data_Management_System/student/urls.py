from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('logout',views.logout_student,name='logout'),
    path('homepage',views.homepage,name='homepage'),
    path('header',views.header,name='header'),

] 

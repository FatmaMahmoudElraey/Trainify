from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]

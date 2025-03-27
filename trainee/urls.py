from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.home, name='home'),
    path('trainee/', views.TraineeListView.as_view(), name='traineelist'),
    path('details/<int:pk>/', views.TraineeDetailView.as_view(), name='trainee_details'),
    path('delete/<int:pk>/', views.TraineeDeleteView.as_view(), name='delete_trainee'),
    path('add/', views.TraineeCreateView.as_view(), name='add_trainee'),
    path('update/<int:pk>/', views.TraineeUpdateView.as_view(), name='update_trainee'),


    path('trainee/api/', views.TraineeListCreateView.as_view(), name='trainee-list-create'),
    path('trainee/api/<int:pk>/', views.TraineeUpdateDeleteView.as_view(), name='trainee-update-delete'),

]

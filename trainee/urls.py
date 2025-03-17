from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('trainee/', views.traineelist, name='traineelist'),
    # path('add/', views.add_trainee, name='add_trainee'),
    # path('update/<int:id>',views.update_trainee, name='update_trainee'),
    # path('delete/<int:id>',views.delete_trainee, name='delete_trainee'),

    path('trainee/', views.TraineeListView.as_view(), name='traineelist'),
    path('details/<int:pk>/', views.TraineeDetailView.as_view(), name='trainee_details'),
    path('delete/<int:pk>/', views.TraineeDeleteView.as_view(), name='delete_trainee'),

    path('add/', views.TraineeCreateView.as_view(), name='add_trainee'),
    path('update/<int:pk>/', views.TraineeUpdateView.as_view(), name='update_trainee'),

]


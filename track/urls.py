from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracks_list, name='tracks_list'),
    path('add/', views.add_track, name='add_track'),
    path('update/<int:id>',views.update_track, name='update_track'),
    path('delete/<int:id>',views.delete_track, name='delete_track'),
]

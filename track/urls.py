from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    tracks_list, add_track, update_track, delete_track,
    TrackViewSet
)

router = SimpleRouter()
router.register(r'tracks', TrackViewSet, basename='track')

urlpatterns = [
    path('', tracks_list, name='tracks_list'),
    path('add/', add_track, name='add_track'),
    path('update/<int:id>/', update_track, name='update_track'),
    path('delete/<int:id>/', delete_track, name='delete_track'),

    path('api/', include(router.urls)), 
]

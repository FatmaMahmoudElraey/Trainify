"""
URL configuration for ITI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('trainee.urls')),
    path('admin/', admin.site.urls),
    path('trainee/', include('trainee.urls')), 
    path('courses/', include('course.urls')), 
    path('tracks/', include('track.urls')), 
    path('accounts/', include('accounts.urls')),
]

# add media image url
from . import settings
# from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
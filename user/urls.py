from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# /user/
router = DefaultRouter()
router.register('profile', views.UserProfileView, basename='profile')


urlpatterns = [
    path('', include(router.urls)),
          
]
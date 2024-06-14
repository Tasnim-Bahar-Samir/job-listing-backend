from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# /user/
router = DefaultRouter()
router.register('profile', views.UserProfileView, basename='profile')
router.register('saved-job', views.SavedJobView, basename='saved-job')


urlpatterns = [
    path('', include(router.urls)),
          
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("register", views.UserRegistrationView, basename="register")

# auth
urlpatterns = [  
    path('', include('dj_rest_auth.urls')),
    path("", include(router.urls)),
]
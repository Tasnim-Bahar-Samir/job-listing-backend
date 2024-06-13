from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("management", views.JobView, basename="management")


urlpatterns = [
    path("", include(router.urls))
]

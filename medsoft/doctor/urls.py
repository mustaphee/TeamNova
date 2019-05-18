from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'doctor'
router = routers.DefaultRouter()
router.register('', views.DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'doctor'
router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('specialities', views.SpecialityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

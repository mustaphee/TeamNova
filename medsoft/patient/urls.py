from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'patient'
router = routers.DefaultRouter()
router.register('patient', views.PatientViewSet, base_name='patient')
router.register('doctor_request', views.DoctorRequestViewSet, base_name='doctor-request')

urlpatterns = [
    path('', include(router.urls)),
]

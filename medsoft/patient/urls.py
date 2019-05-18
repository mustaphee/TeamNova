from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'patient'
router = routers.DefaultRouter()
router.register('', views.PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

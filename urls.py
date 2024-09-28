

from django.contrib import admin
from django.urls import path
from rest_framework import routers
from Managment_System.views import HospitalViewSet,DoctorViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register('hospital', HospitalViewSet)
router.register('doctor',DoctorViewSet)

urlpatterns += router.urls


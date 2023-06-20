from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

# Router will help in mapping the URLs to the desired views
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    # Blank URL means companies will be accessible at the root URL
    path('', include(router.urls))
]

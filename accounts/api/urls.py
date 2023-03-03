from django.urls import path, include
from accounts.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewset)
router.register(r'companies', api_views.CompanyViewset)
router.register(r'profiles', api_views.ProfileViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]
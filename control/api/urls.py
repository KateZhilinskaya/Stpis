from django.urls import path, include
from control.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'providers', api_views.ProviderViewset)
router.register(r'products', api_views.ProductViewset)
router.register(r'provider-products', api_views.ProviderProductViewset)
router.register(r'in-contracts', api_views.InternalContractViewset)
router.register(r'ex-contracts', api_views.ExternalContractViewset)
router.register(r'applications', api_views.ApplicationViewset)
router.register(r'requirements', api_views.RequirementViewset)
router.register(r'orders', api_views.OrderViewset)
router.register(r'order-parts', api_views.OrderPartViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
]
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from control.models import *
from control.api.serializers import *


class ProviderViewset(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProductSerializer

    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
class ProviderProductViewset(viewsets.ModelViewSet):
    queryset = ProviderProduct.objects.all()
    serializer_class = ProviderProductSerializer


class InternalContractViewset(viewsets.ModelViewSet):
    queryset = InternalContract.objects.all()
    serializer_class = InternalContractSerializer


class ExternalContractViewset(viewsets.ModelViewSet):
    queryset = ExternalContract.objects.all()
    serializer_class = ExternalContractSerializer


class ApplicationViewset(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class RequirementViewset(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderPartViewset(viewsets.ModelViewSet):
    queryset = OrderPart.objects.all()
    serializer_class = OrderPartSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from control.models import *


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ['id', 'name', 'company', 'contract']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'company']


class ProviderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderProduct
        fields = ['id', 'provider', 'product', 'cost']


class InternalContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternalContract
        fields = ['id', 'contract', 'company', 'date']


class ExternalContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalContract
        fields = ['id', 'contract', 'company', 'provider', 'date']


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'contract', 'company', 'status', 'date']


class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = ['id', 'product', 'amount', 'application']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'company', 'date', 'status', 'cost']


class OrderPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderPart
        fields = ['id', 'requirement', 'order', 'contract', 'product', 'amount', 'cost', 'address', 'fio']
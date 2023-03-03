from django.contrib import admin
from .models import *

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "company"]
    readonly_fields = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ('id',)


@admin.register(ProviderProduct)
class ProviderProductAdmin(admin.ModelAdmin):
    list_display = ["provider", "product", "cost"]
    readonly_fields = ('id',)


@admin.register(InternalContract)
class InternalContractAdmin(admin.ModelAdmin):
    list_display = ["contract", "company", "date"]
    readonly_fields = ('id',)


@admin.register(ExternalContract)
class ExternalContractAdmin(admin.ModelAdmin):
    list_display = ["contract", "company", "provider", "date"]
    readonly_fields = ('id',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["company", "date", "status"]
    readonly_fields = ('id',)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ["product", "amount", "application"]
    readonly_fields = ('id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["company", "date", "cost"]
    readonly_fields = ('id',)


@admin.register(OrderPart)
class OrderPartAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "amount", "cost"]
    readonly_fields = ('id',)



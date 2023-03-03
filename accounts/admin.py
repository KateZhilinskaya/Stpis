from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "patronymic", "status"]
    readonly_fields = ('id',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["owner", "name"]
    readonly_fields = ('id',)




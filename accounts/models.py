from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    owner = models.OneToOneField(User, verbose_name="Владелец", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Компании"
        verbose_name = "Компания"


class Profile(models.Model):

    STATUS_CHOICE = {
        (0, "Сотрудник"),
        (1, "Отдел закупок"),
        (2, "Владелец")
    }

    
    user = models.OneToOneField(User, verbose_name="пользователь", on_delete=models.CASCADE)
    patronymic = models.CharField("Отчество", max_length=64, blank=True, null=True)
    status = models.IntegerField("Должность", choices=STATUS_CHOICE)
    company = models.ForeignKey(Company, verbose_name="Компания", related_name='profiles', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email}: {self.get_status_display()}"

    def get_fio(self):
        return f"{self.user.last_name} {self.user.first_name} {self.patronymic or ''}"

    class Meta:
        verbose_name_plural = "Профили"
        verbose_name = "Профиль"

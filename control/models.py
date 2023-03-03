from django.db import models
from accounts.models import Company
from django.conf import settings


class Provider(models.Model):

    name = models.CharField("Название", max_length=255)
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="providers", on_delete=models.CASCADE)
    contract = models.FileField(upload_to="contacts", null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.company.name}"
    
    class Meta:
        verbose_name_plural = "Поставщики"
        verbose_name = "Поставщик"


class Product(models.Model):

    name = models.CharField("Название", max_length=255)
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"


class ProviderProduct(models.Model):

    provider = models.ForeignKey(Provider, verbose_name="Поставщик", related_name="products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Товар", related_name="providers", on_delete=models.CASCADE)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.provider.name}({self.product.name}): {self.cost}"
    
    class Meta:
        verbose_name_plural = "Товары поставщиков"
        verbose_name = "Товар поставщика"


class InternalContract(models.Model):

    contract = models.FileField("Договор", upload_to="contracts/internal")
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="internal_contracts", on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.company.name}: {self.date.strftime('%d/%m/%y %H:%M:%S')}"
    
    class Meta:
        verbose_name_plural = "Внутренние договоры"
        verbose_name = "Внутренний договор"


class ExternalContract(models.Model):

    contract = models.FileField("Договор", upload_to="contracts/external")
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="external_contracts", on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, verbose_name="Поставщик", related_name="contracts", on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.company.name}-{self.provider.name}: {self.date.strftime('%d/%m/%y %H:%M:%S')}"
    
    class Meta:
        verbose_name_plural = "Внешние договоры"
        verbose_name = "Внешние договор"


class Application(models.Model):

    STATUS_CHOICE = {
        (0, "Cоздана"),
        (1, "Отправлена"),
        (2, "Принята"),
        (3, "Завершена"),
        (4, "Отклонена")
    }

    company = models.ForeignKey(Company, verbose_name="Компании", related_name="applications", on_delete=models.CASCADE)
    contract = models.OneToOneField(InternalContract, verbose_name="Внутренний контракт", on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField("Дата")
    status = models.IntegerField("Статус", choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"Заявка {self.company.name}: {self.date.strftime('%d/%m/%y %H:%M:%S')}"
    
    class Meta:
        verbose_name_plural = "Заявки"
        verbose_name = "Заявка"


class Requirement(models.Model):

    product = models.ForeignKey(Product, verbose_name="Продукт", related_name="requirements", on_delete=models.CASCADE)
    amount = models.IntegerField()
    application = models.ForeignKey(Application, verbose_name="Заявка", related_name="requirements", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.company.name}: {self.product.name}({self.amount})"
    
    class Meta:
        verbose_name_plural = "Требования"
        verbose_name = "Требование"


class Order(models.Model):

    STATUS_CHOICE = {
        (0, "Создан"),
        (1, "Сформирован"),
    }

    company = models.ForeignKey(Company, verbose_name="Компании", related_name="orders", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата")
    cost = models.FloatField("Цена", null=True, blank=True)
    status = models.IntegerField("Статус", choices=STATUS_CHOICE, default=0)

    def is_ready(self):
        return all([part.cost for part in self.parts.all()])

    def __str__(self):
        return f"Заказ {self.company.name}: {self.date.strftime('%d/%m/%y %H:%M:%S')} - {self.cost}"
    
    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"


class OrderPart(models.Model):

    requirement = models.OneToOneField(Requirement, verbose_name="Требование", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="Заказ", related_name="parts", on_delete=models.CASCADE)
    contract = models.OneToOneField(ExternalContract, verbose_name="Внешний контракт", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProviderProduct, verbose_name="Товар", related_name="order_parts", on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField("Кол-во", null=True, blank=True)
    cost = models.FloatField("Цена", null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, null=True, blank=True)
    fio = models.CharField("ФИО получателя", max_length=255, null=True, blank=True)

    def __str__(self):
        if self.product:
            return f"Часть заказа: {self.product.product.name}({self.amount}) - {self.cost}"
        return f"Часть заказы для {self.requirement}"
    
    class Meta:
        verbose_name_plural = "Части заказов"
        verbose_name = "Часть заказа"


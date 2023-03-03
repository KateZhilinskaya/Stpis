from django import forms
from .models import *


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = ("name", "contract")
        widgets = {'contract': forms.FileInput}

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {"placeholder": "Название"}
            )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {"placeholder": "Название"}
            )


class ProviderProductForm(forms.ModelForm):

    class Meta:
        model = ProviderProduct
        fields = ("product", "cost")

    def __init__(self, *args, **kwargs):
        super(ProviderProductForm, self).__init__(*args, **kwargs)

        self.fields['cost'].widget.attrs.update(
            {"placeholder": "Цена"}
            )


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ("product", "amount")

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs.update(
            {"placeholder": "Кол-во"}
            )


class OrderPartForm(forms.ModelForm):

    class Meta:
        model = OrderPart
        fields = ("product", "amount", "address", "fio")

    def __init__(self, *args, **kwargs):
        super(OrderPartForm, self).__init__(*args, **kwargs)

        # self.fields["product"] = forms.ChoiceField(
        #     choices=tuple([(product.pk, product) for product in ProviderProduct.objects.all()])
        # )

        self.fields['amount'].widget.attrs.update(
            {"placeholder": "Кол-во"}
            )
        self.fields['address'].widget.attrs.update(
            {"placeholder": "Адрес"}
            )
        self.fields['fio'].widget.attrs.update(
            {"placeholder": "ФИО"}
            )


class InternalContractForm(forms.ModelForm):

    class Meta:
        model = InternalContract
        fields = ("contract", )

    def __init__(self, *args, **kwargs):
        super(InternalContractForm, self).__init__(*args, **kwargs)


class ExternalContractForm(forms.ModelForm):

    class Meta:
        model = ExternalContract
        fields = ("contract", )

    def __init__(self, *args, **kwargs):
        super(ExternalContractForm, self).__init__(*args, **kwargs)

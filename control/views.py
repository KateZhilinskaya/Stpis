from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import *
from .forms import *
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime as dt


def index(request):
    return redirect(reverse("edit"))


class StaffView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status != 2:
            return HttpResponse("No permission")
            # return redirect(reverse())
        
        company = user.company
        staff = company.profiles.all()

        return render(
            request,
            "control/staff.html",
            {
                "staff": staff
            }
        )


class EmployeeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return HttpResponse("No permission")

        company = user.company
        employee = User.objects.get(id=kwargs["uid"])
        if employee.profile.company != company:
            return HttpResponse("No permission")

        user_form = OwnerUserEditForm(instance=employee, data=request.POST)
        profile_form = EmployeeForm(instance=employee.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return redirect(reverse("employee", kwargs={'uid':kwargs["uid"]}))

        

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status != 2:
            return HttpResponse("No permission")
            # return redirect(reverse())
        
        company = user.company
        employee = User.objects.get(id=kwargs["uid"])

        if employee.profile.company != company:
            return HttpResponse("No permission")

        user_form = OwnerUserEditForm(instance=employee)
        profile_form = EmployeeForm(instance=employee.profile)

        return render(
            request,
            "control/employee.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "employee": employee,
            }
        )
        

class AddEmployeeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return HttpResponse("No permission")

        company = user.company

        user_form = UserForm(data=request.POST)
        profile_form = EmployeeForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            cd = user_form.cleaned_data
            # отправляем письмо на почту новому пользователю
            message = f"Логин: {cd.get('email')}\nПароль: {cd.get('password')}"
            send_mail("Вы зарегистрированы", message, settings.EMAIL_HOST_USER, [cd.get("email")])

            new_user = user_form.save(commit=False)
            new_user.username = new_user.email
            new_user.set_password(cd.get("password"))
            new_user.save()

            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.company = company
            new_profile.save()


        return redirect(reverse("add_employee"))

        

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status != 2:
            return HttpResponse("No permission")
            # return redirect(reverse())

        user_form = UserForm()
        profile_form = EmployeeForm()

        return render(
            request,
            "control/add_employee.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
            }
        )


def delete_employee(request, uid):
    user = request.user
    if user.profile.status != 2:
        return HttpResponse("No permission")

    employee = User.objects.get(id=uid)
    if employee.profile.company != user.company:
        return HttpResponse("No permission")

    employee.delete()
    return redirect(reverse("staff"))


class ProvidersView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.profile.status == 0:
            return HttpResponse("No permission")
            # return redirect(reverse())
        
        providers = user.profile.company.providers.all()

        return render(
            request,
            "control/providers.html",
            {
                "providers": providers
            }
        )


class ProviderView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("providers"))

        provider = Provider.objects.get(id=kwargs["uid"])

        form = ProviderForm(instance=provider, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        return redirect(reverse("providers"))

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status == 0:
            return redirect(reverse("providers"))

        provider = Provider.objects.get(id=kwargs["uid"])

        form = None
        product_form = None
        if user.profile.status == 2:
            form = ProviderForm(instance=provider)
            product_form = ProviderProductForm()


        return render(
            request,
            "control/provider.html",
            {
                "provider": provider,
                "form": form,
                "product_form": product_form,
            }
        )


class AddProviderView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("providers"))

        form = ProviderForm(request.POST, request.FILES)
        if form.is_valid():
            new_provider = form.save(commit=False)
            new_provider.company = user.company
            new_provider.save()

        return redirect(reverse("add_provider"))

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("providers"))

        form = ProviderForm()

        return render(
            request,
            "control/add_provider.html",
            {
                "form": form,
            }
        )


class AddProviderProductView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("providers"))

        provider = Provider.objects.get(id=kwargs["uid"])
        if user.company != provider.company:
            return redirect(reverse("providers"))

        form = ProviderProductForm(request.POST)
        if form.is_valid():
            new_provider_product = form.save(commit=False)
            new_provider_product.provider = provider
            new_provider_product.save()

        return redirect(reverse("provider", kwargs={"uid": kwargs["uid"]}))


def delete_provider(request, uid):
    user = request.user
    if user.profile.status != 2:
        return HttpResponse("No permission")

    provider = Provider.objects.get(id=uid)
    if provider.company != user.company:
        return HttpResponse("No permission")

    provider.delete()
    return redirect(reverse("providers"))


class ProductsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        
        products = user.profile.company.products.all()

        return render(
            request,
            "control/products.html",
            {
                "products": products
            }
        )


class ProductView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("products"))

        product = Product.objects.get(id=kwargs["uid"])

        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse("products"))

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status == 0:
            return redirect(reverse("products"))

        product = Product.objects.get(id=kwargs["uid"])

        form = None
        if user.profile.status == 2:
            form = ProductForm(instance=product)

        return render(
            request,
            "control/product.html",
            {
                "product": product,
                "form": form,
            }
        )


class AddProductView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("products"))

        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.company = user.company
            new_product.save()

        return redirect(reverse("add_product"))

    def get(self, request, *args, **kwargs):
        
        user = request.user
        if user.profile.status != 2:
            return redirect(reverse("products"))

        form = ProductForm()

        return render(
            request,
            "control/add_product.html",
            {
                "form": form,
            }
        )


def delete_product(request, uid):
    user = request.user
    if user.profile.status != 2:
        return HttpResponse("No permission")

    product = Product.objects.get(id=uid)
    if product.company != user.company:
        return HttpResponse("No permission")

    product.delete()
    return redirect(reverse("products"))


class ApplicationsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        user = request.user

        applications = Application.objects.filter(company=user.profile.company).filter(status__in=[0, 1, 2]).all()
        if user.profile.status == 1:
            applications = applications.filter(status__in=[1, 2])

        return render(
            request,
            "control/applications.html",
            {
                "applications": applications,
            }
        )


def add_application(request):

    user = request.user
    company = user.profile.company
    new_application = Application.objects.create(
        company=company,
        date=dt.now()
    )
    new_application.save()

    return redirect(reverse("applications"))


class ApplicationView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        form = RequirementForm(request.POST)
        application = Application.objects.get(id=kwargs["uid"])

        if application.company != user.profile.company:
            return HttpResponse("No permission")

        if form.is_valid():
            new_requirement = form.save(commit=False)
            new_requirement.application = application
            new_requirement.save()
        
        return redirect(reverse("application", kwargs={"uid": kwargs["uid"]}))


    def get(self, request, *args, **kwargs):
        
        user = request.user
        form = RequirementForm()
        application = Application.objects.get(id=kwargs["uid"])
        if application.contract:
            contract_form = InternalContractForm(instance=application.contract)
        else:
            contract_form = InternalContractForm()

        if application.company != user.profile.company:
            return HttpResponse("No permission")


        return render(
            request,
            "control/application.html",
            {
                "form": form,
                "application": application,
                "contract_form": contract_form,
            }
        )


def add_internal_contract(request, uid):

    user = request.user
    application = Application.objects.get(id=uid)

    if user.profile.company != application.company:
        return HttpResponse("No permission")

    if application.contract:
        form = InternalContractForm(instance=application.contract, data=request.POST, files=request.FILES)
    else:
        form = InternalContractForm(request.POST, request.FILES)

    if form.is_valid():
        new_contract = form.save(commit=False)
        new_contract.company = application.company
        new_contract.date = dt.now()
        new_contract.save()
        application.contract = new_contract
        application.save()

    return redirect(reverse("application", kwargs={"uid": uid}))


def add_external_contract(request, uid):

    user = request.user
    part = OrderPart.objects.get(id=uid)
    company = part.requirement.application.company

    if user.profile.company != company:
        return HttpResponse("No permission")

    if part.contract:
        form = ExternalContractForm(instance=part.contract, data=request.POST, files=request.FILES)
    else:
        form = ExternalContractForm(request.POST, request.FILES)

    if form.is_valid():
        new_contract = form.save(commit=False)
        new_contract.company = company
        new_contract.provider = part.product.provider
        new_contract.date = dt.now()
        new_contract.save()
        part.contract = new_contract
        part.save()

    return redirect(reverse("order", kwargs={"uid": part.requirement.application.id}))


def send_application(request, uid):

    user = request.user
    application = Application.objects.get(id=uid)
    if user.profile.company != application.company:
        return HttpResponse("No permission")

    application.status = 1
    application.save()

    return redirect(reverse("applications"))


def accept_application(request, uid):

    user = request.user
    if user.profile.status == 0:
        return HttpResponse("No permission")
    
    application = Application.objects.get(id=uid)
    if user.profile.company != application.company:
        return HttpResponse("No permission")

    application.status = 2
    application.save()

    order = Order.objects.create(
        company=user.profile.company,
        date=dt.now()
    )
    order.save()
    for requirement in application.requirements.all():
        order_part = OrderPart.objects.create(
            requirement=requirement,
            order=order,
        )
        order_part.save()

    return redirect(reverse("order", kwargs={"uid": uid}))


def reject_application(request, uid):
    user = request.user
    if user.profile.status == 0:
        return HttpResponse("No permission")

    application = Application.objects.get(id=uid)
    if user.profile.company != application.company:
        return HttpResponse("No permission")

    application.status = 4
    application.save()
    return redirect(reverse("applications"))


def delete_requirement(request, uid):

    user = request.user
    requirement = Requirement.objects.get(id=uid)
    if user.profile.company != requirement.application.company:
        return HttpResponse("No permission")

    requirement.delete()
    return redirect(reverse("application", kwargs={"uid": requirement.application.id}))


class OrderView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user = request.user
        order = Application.objects.get(id=kwargs["uid"]).requirements.first().orderpart.order

        if user.profile.company != order.company:
            return HttpResponse("No permission")
        
        return render(
            request,
            "control/order.html",
            {
                "order": order,
            }
        )


class OrderPartView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        part = OrderPart.objects.get(id=kwargs["uid"])

        if user.profile.company != part.order.company:
            return HttpResponse("No permission")

        form = OrderPartForm(instance=part, data=request.POST)
        if form.is_valid():
            updated_part = form.save(commit=False)
            updated_part.cost = updated_part.product.cost * updated_part.amount
            updated_part.save()

        return redirect(reverse("order", kwargs={"uid": part.requirement.application.id}))

    def get(self, request, *args, **kwargs):

        user = request.user
        part = OrderPart.objects.get(id=kwargs["uid"])
        
        if user.profile.company != part.order.company:
            return HttpResponse("No permission")
        
        if part.order.status == 1:
            return redirect(reverse("archive"))

        form = OrderPartForm(instance=part)
        if part.contract:
            contract_form = ExternalContractForm(instance=part.contract)
        else:
            contract_form = ExternalContractForm()

        return render(
            request,
            "control/order_part.html",
            {
                "part": part,
                "form": form,
                "contract_form": contract_form
            }
        )


def form_order(request, uid):

    user = request.user
    order = Order.objects.get(id=uid)

    if user.profile.company != order.company:
        return HttpResponse("No permission")
    
    order.status = 1
    order.save()

    application = order.parts.first().requirement.application
    application.status = 3
    application.save()

    return redirect(reverse("applications"))


class ArchiveView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user = request.user
        if user.profile.status == 1:
            applications = Application.objects.filter(company=user.profile.company).filter(status=3).all()
        else:
            applications = Application.objects.filter(company=user.profile.company).filter(status__in=[3, 4]).all()
            
        return render(
            request,
            "control/archive.html",
            {
                "applications": applications,
            }
        )
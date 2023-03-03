from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        company_form = CompanyForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and company_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.username = new_user.email
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            new_company = company_form.save(commit=False)
            new_company.owner = new_user
            new_company.save()

            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.status = 2
            new_profile.company = new_company
            new_profile.save()

            new_user = authenticate(username=user_form.cleaned_data['email'],
                                    password=user_form.cleaned_data['password'],
                                    )
            login(request, new_user)

            return redirect(reverse("edit"))

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        company_form = CompanyForm()

    return render(
        request, 
        "accounts/registration.html", 
        {
            "user_form": user_form, 
            "profile_form": profile_form,
            "company_form": company_form,
        }
    )


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["email"], password=cd["password"]
            )
            if user is None:
                messages.info(request, "E-mail или пароль введены неверно")
                return redirect(reverse("login"))

            if not user.is_active:
                messages.info(request, "Вы заблокированы")
                return redirect(reverse("login"))

            login(request, user)
            return redirect(reverse("edit"))

        return render(request, "accounts/login.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})


@login_required
def edit(request):

    if request.user.profile.status != 2:
        if request.method == "POST":
            user_form = UserEditForm(instance=request.user, data=request.POST)
            if user_form.is_valid():
                user_form.save()
            return redirect(reverse("edit"))

        user_form = UserEditForm(instance=request.user)
        return render(
            request,
            "accounts/account.html",
            {
                "user_form": user_form,
            }
        )

    if request.method == "POST":
        user_form = OwnerUserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        company_form = CompanyForm(instance=request.user.company, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid() and company_form.is_valid():
            user_form.save()
            profile_form.save()
            company_form.save()

        return redirect(reverse("edit"))

    else:
        user_form = OwnerUserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        company_form = CompanyForm(instance=request.user.company)
    
    return render(
        request,
        "accounts/account.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "company_form": company_form,
        }
    )


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path('staff/', views.StaffView.as_view(), name="staff"),
    path('employee/<int:uid>/', views.EmployeeView.as_view(), name="employee"),
    path('employee/add/', views.AddEmployeeView.as_view(), name="add_employee"),
    path('employee/delete/<int:uid>/', views.delete_employee, name="delete_employee"),

    path('providers/', views.ProvidersView.as_view(), name="providers"),
    path('provider/add/', views.AddProviderView.as_view(), name="add_provider"),
    path('provider/<int:uid>/', views.ProviderView.as_view(), name="provider"),
    path('provider/<int:uid>/product/add/', views.AddProviderProductView.as_view(), name="add_provider_product"),
    path('provider/delete/<int:uid>/', views.delete_provider, name="delete_provider"),

    path('products/', views.ProductsView.as_view(), name="products"),
    path('product/<int:uid>/', views.ProductView.as_view(), name="product"),
    path('product/add/', views.AddProductView.as_view(), name="add_product"),
    path('product/delete/<int:uid>/', views.delete_product, name="delete_product"),

    path('applications/', views.ApplicationsView.as_view(), name="applications"),
    path('application/<int:uid>/', views.ApplicationView.as_view(), name="application"),
    path('application/add/', views.add_application, name="add_application"),
    path('application/<int:uid>/send/', views.send_application, name="send_application"),
    path('application/<int:uid>/accept/', views.accept_application, name="accept_application"),
    path('application/<int:uid>/reject/', views.reject_application, name="reject_application"),
    path('requirement/delete/<int:uid>/', views.delete_requirement, name="delete_requirement"),

    path('order/<int:uid>/', views.OrderView.as_view(), name="order"),
    path('order_part/<int:uid>/', views.OrderPartView.as_view(), name="order_part"),
    path('order/form/<int:uid>/', views.form_order, name="form_order"),

    path('archive/', views.ArchiveView.as_view(), name="archive"),

    path('contracts/internal/add/<int:uid>', views.add_internal_contract, name="internal_contract_add"),
    path('contracts/external/add/<int:uid>', views.add_external_contract, name="external_contract_add"),

]
"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from domain.views import base, person, customer, auth

urlpatterns = [
    path(
        '',
        base.domain_base,
        name="domain"
    ),
    path(
        'login/',
        auth.user_login,
        name="user_login"
    ),
    path(
        'logout/',
        auth.user_logout,
        name="user_logout"
    ),
    path(
        'person/',
        person.person_list,
        name="persons"
    ),
    path(
        'person/create',
        person.create_person,
        name="person_create"
    ),
    path(
        'person/<str:person_id>',
        person.get_or_update_person_details,
        name="person"
    ),
    path(
        'person/<str:person_id>/delete',
        person.delete_person,
        name="person_delete"
    ),
    path(
        'customer/',
        customer.customer_list,
        name="customers"
    ),
    path(
        'customer/create',
        customer.create_customer,
        name="customer_create"
    ),
    path(
        'customer/<str:customer_id>',
        customer.get_or_update_customer_details,
        name="customer"
    ),
    path(
        'customer/<str:customer_id>/delete',
        customer.delete_customer,
        name="customer_delete"
    ),
]

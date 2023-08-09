from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from domain.models import Payment, Customer, Person


# Create your views here.


@login_required(login_url="user_login")
def domain_base(request):
    orders_count = Payment.objects.all().count()
    customers_count = Customer.objects.all().count()
    persons_count = Person.objects.all().count()
    context = {
        "orders_count": orders_count,
        "customers_count": customers_count,
        "persons_count": persons_count,
    }
    return render(request, "domain/index.html", context)

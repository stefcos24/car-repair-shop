from django.shortcuts import render
from ..models.customer import Customer

# Create your views here.


def get_all_customers(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'domain/customers.html', context)

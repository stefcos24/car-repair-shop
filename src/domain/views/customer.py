import datetime
import uuid

from django.shortcuts import render, redirect

from domain.forms.customer import CustomerForm
from domain.models.customer import Customer

# Create your views here.


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'domain/customers.html', context)


def customer_details(request, customer_id: uuid.UUID):
    customer = Customer.objects.filter(id=customer_id).first()
    context = {
        "customer": customer
    }
    return render(request, 'domain/customer.html', context)


def create_customer(request):

    form = CustomerForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            full_name = f"{first_name} {last_name}"
            address1 = form.cleaned_data["address1"]
            address2 = form.cleaned_data["address2"]
            city = form.cleaned_data["city"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            jib = form.cleaned_data["email"]
            pib = form.cleaned_data["email"]
            active = form.cleaned_data["active"]
            created = datetime.datetime.now()
            modified = datetime.datetime.now()

            customer = Customer(
                id=uuid.uuid4(),
                full_name=full_name,
                first_name=first_name,
                last_name=last_name,
                address1=address1,
                address2=address2,
                city=city,
                phone_number=phone_number,
                email=email,
                jib=jib,
                pib=pib,
                created=created,
                modified=modified,
                active=active
            )
            customer.save()
            return redirect('customers')
    return render(request, 'domain.customers.html')
import datetime
import uuid

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from domain.forms.customer import CustomerForm
from domain.models.customer import Customer

# Create your views here.


@login_required(login_url='user_login')
def customer_list(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'domain/customers.html', context)


@login_required(login_url='user_login')
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
            messages.success(request, 'Customer is created successfully!')
            return redirect('customers')

    context = {
        "form": form
    }

    return render(request, 'domain/customer_create.html', context)


@login_required(login_url='user_login')
def get_or_update_customer_details(request, customer_id: uuid.UUID):

    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        raise Http404()

    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.instance.modified = datetime.datetime.now()
            form.save()
            messages.success(request, 'Customer is updated successfully!')
            return redirect('customers')

    context = {
        "form": form,
        "customer": customer
    }
    return render(request, 'domain/customer.html', context)


@login_required(login_url='user_login')
def delete_customer(request, customer_id: uuid.UUID):

    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        raise Http404()

    if request.method == "POST":
        customer.delete()
        messages.success(request, 'Customer is deleted successfully!')
        return redirect('customers')

    context = {
        "customer": customer
    }
    return render(request, 'domain/customer_delete.html', context)

import uuid

from django.shortcuts import render, redirect
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
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        jib=request.POST.get('jib')
        pib=request.POST.get('pib')
        
        customer=Customer(
            id=uuid.uuid4(),
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            address1=address1,
            address2=address2,
            city=city,
            phone_number=phone_number,
            email=email,
            JIB=jib,
            PIB=pib
        )
        customer.save()
        return redirect('customers')
    return render(request, 'domain.customers.html')
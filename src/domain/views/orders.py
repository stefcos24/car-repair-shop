import datetime
import json
import uuid

from django.http import Http404
from django.shortcuts import redirect, render

from domain.models import Customer, Payment, PaymentsItem, PaymentsDetail


def safe_float_conversion(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default


def get_orders(request):
    orders = Payment.objects.all()
    context = {"orders": orders}
    return render(request, "domain/orders.html", context)


def get_order(request, order_id: uuid.UUID):
    order = Payment.objects.filter(id=order_id).first()
    order_items = PaymentsItem.objects.filter(payment_id=order_id).all()
    print(order_items)
    if not order:
        raise Http404()
    context = {"order": order, "order_items": order_items}
    return render(request, "domain/order.html", context)


def create_order(request):
    if request.method == "POST":
        person = request.user.person
        customer_id = request.POST.get("customer")
        payment_method = request.POST.get("payment_method")
        vehicle = request.POST.get("vehicle")
        plate_number = request.POST.get("plate_number")

        items = []
        prices = []
        discounts = []
        total_prices = []

        i = 0
        while True:
            item_key = f"item[{i}]"
            price_key = f"price[{i}]"
            discount_key = f"discount[{i}]"
            total_price_key = f"total_price[{i}]"

            if not request.POST.get(item_key):
                break

            items.append(request.POST.get(item_key, "0"))
            prices.append(request.POST.get(price_key, "0"))
            discounts.append(request.POST.get(discount_key, "0"))
            total_prices.append(request.POST.get(total_price_key, "0"))

            i += 1
        content = [
            {
                "item": item,
                "price": safe_float_conversion(price),
                "discount": safe_float_conversion(discount),
                "total_price": safe_float_conversion(total_price),
            }
            for item, price, discount, total_price in zip(
                items, prices, discounts, total_prices
            )
        ]

        total_amount = sum([item["total_price"] for item in content])

        last_payment = Payment.objects.all().order_by("-bill_id").first()

        if last_payment:
            new_bill_id = last_payment.bill_id + 1
        else:
            new_bill_id = 1

        # create PaymentsDetail instance
        payment_details = PaymentsDetail.objects.create(
            id=uuid.uuid4(),
            total_amount=str(total_amount),
            created=datetime.datetime.now(),
            modified=datetime.datetime.now(),
        )

        customer = Customer.objects.get(pk=customer_id)

        payment = Payment.objects.create(
            id=uuid.uuid4(),
            person=person,
            bill_id=new_bill_id,
            payments_details=payment_details,
            customer=customer,
            vehicle=vehicle,
            vehicle_plate_number=plate_number,
            date_of_issue=datetime.datetime.now(),
            value_date=datetime.datetime.now(),
            delivery_date=datetime.datetime.now(),
            payment_method=payment_method,
            content=content,
        )

        for item in content:
            PaymentsItem.objects.create(
                id=uuid.uuid4(),
                payment=payment,
                content_item=item,
                created=datetime.datetime.now(),
                modified=datetime.datetime.now(),
            )
        # TODO in future will be redirect to invoice doc
        return redirect("orders")

    customers = Customer.objects.all()
    context = {"customers": customers}

    return render(request, "domain/order_create.html", context)

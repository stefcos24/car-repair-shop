from django.contrib import admin
from domain.models.person import Person
from domain.models.customer import Customer
from domain.models.payments_details import PaymentsDetail
from domain.models.payments import Payment
from domain.models.payments_items import PaymentsItem


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "active"]
    readonly_fields = ["created", "modified"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "address1", "email", "phone_number", "active"]
    readonly_fields = ["created", "modified"]


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ["id", "bill_id", "date_of_issue", "value_date", "payment_method"]


@admin.register(PaymentsDetail)
class PaymentsDetailsAdmin(admin.ModelAdmin):
    list_display = ["id", "total_amount"]
    readonly_fields = ["created", "modified"]


@admin.register(PaymentsItem)
class PaymentsItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "payment"]
    readonly_fields = ["created", "modified"]

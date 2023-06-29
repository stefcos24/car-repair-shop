from django.contrib import admin
from .models.person import *
from .models.customer import *
from .models.payments_details import *
from .models.payments import *
from .models.payments_items import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Payments_details)
admin.site.register(Payments)
admin.site.register(Payments_items)
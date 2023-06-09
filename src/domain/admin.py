from django.contrib import admin
from .models.person import *
from .models.customer import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Customer)
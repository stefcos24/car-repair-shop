from domain.views.base import domain_base
from domain.views.customer import (
    customer_list,
    get_or_update_customer_details,
    create_customer,
)
from domain.views.person import (
    person_list,
    create_person,
    get_or_update_person_details,
    delete_person,
)
from domain.views.auth import user_login, user_logout
from domain.views.orders import create_order, get_order, get_orders
from domain.views.error import error_404_view, error_500_view

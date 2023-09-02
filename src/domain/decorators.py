from django.shortcuts import redirect, render

from domain.models import Person


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("domain")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles: list):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, "domain/403.html", status=403)

        return wrapper_func

    return decorator


def staff_or_admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        is_staff = request.user.groups.filter(name="staff").exists()
        is_admin = request.user.groups.filter(name="admin").exists()

        if request.method == "POST":
            if not (is_staff or is_admin):
                return render(request, "domain/403.html", status=403)

            if is_staff and not is_admin:
                person_id = kwargs.get("person_id")
                person = Person.objects.filter(id=person_id).first()

                if not person or person.user != request.user:
                    return render(request, "domain/403.html", status=403)

        return view_func(request, *args, **kwargs)

    return wrapper_func

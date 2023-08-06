from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('domain')
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
                return render(request, 'domain/403.html', status=403)
        return wrapper_func
    return decorator

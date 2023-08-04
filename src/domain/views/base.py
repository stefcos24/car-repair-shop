from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='user_login')
def domain_base(request):
    return render(request, 'domain/index.html')

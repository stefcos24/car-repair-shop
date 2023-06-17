from django.shortcuts import render

# Create your views here.


def domain_base(request):
    return render(request, 'domain/index.html')

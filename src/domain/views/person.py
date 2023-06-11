from django.shortcuts import render
from ..models.person import Person

# Create your views here.


def get_all_persons(request):
    persons = Person.objects.all()
    context = {
        "persons1234": persons
    }
    return render(request, 'domain/persons.html', context)

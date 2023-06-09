import uuid

from django.shortcuts import render, redirect
from ..models.person import Person


def person_list(request):
    persons = Person.objects.all()
    context = {
        "persons": persons
    }
    return render(request, 'domain/persons.html', context)


def person_details(request, person_id: uuid.UUID):
    person = Person.objects.filter(id=person_id).first()
    context = {
        "person": person
    }
    return render(request, 'domain/person.html', context)


def create_person(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        person = Person(
            id=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )
        person.save()
        return redirect('persons')
    return render(request, 'domain/persons.html')

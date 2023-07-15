import datetime
import uuid

from django.shortcuts import render, redirect
from domain.models.person import Person
from domain.forms.person import PersonForm


def person_list(request):
    persons = Person.objects.all()
    context = {
        "persons": persons
    }
    return render(request, 'domain/persons.html', context)


def create_person(request):
    form = PersonForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            active = form.cleaned_data["active"]
            created = datetime.datetime.now()
            modified = datetime.datetime.now()

            person = Person(
                id=uuid.uuid4(),
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                active=active,
                created=created,
                modified=modified
            )
            person.save()
            return redirect('persons')

    context = {
        "form": form
    }
    return render(request, 'domain/person_create.html', context)


def get_or_update_person_details(request, person_id: uuid.UUID):

    person = Person.objects.filter(id=person_id).first()

    form = PersonForm(instance=person)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.instance.modified = datetime.datetime.now()
            form.save()
            return redirect('persons')

    context = {
        "form": form,
        "person": person
    }
    return render(request, 'domain/person.html', context)


def delete_person(request, person_id: uuid.UUID):

    person = Person.objects.filter(id=person_id).first()

    if request.method == "POST":
        person.delete()
        return redirect('persons')

    context = {
        "person": person
    }
    return render(request, 'domain/person_delete.html', context)

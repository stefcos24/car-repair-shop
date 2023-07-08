import uuid

from django.shortcuts import render, redirect
from ..models.person import Person
from ..forms.person import PersonForm


def person_list(request):
    persons = Person.objects.all()
    context = {
        "persons": persons
    }
    return render(request, 'domain/persons.html', context)


def create_person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.id = uuid.uuid4()
            person.save()
            return redirect('persons')

    context = {
        "form": form
    }
    return render(request, 'domain/person_create.html', context)


def get_or_update_person_details(request, person_id):

    person = Person.objects.filter(id=person_id).first()

    form = PersonForm(instance=person)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person', person_id=person.id)

    context = {
        "form": form,
        "person": person
    }
    return render(request, 'domain/person.html', context)


def delete_person(request, person_id):

    person = Person.objects.filter(id=person_id).first()

    if request.method == "POST":
        person.delete()
        return redirect('persons')

    context = {
        "person": person
    }
    return render(request, 'domain/person_delete.html', context)

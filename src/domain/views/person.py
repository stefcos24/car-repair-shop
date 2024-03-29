import datetime
import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from domain.decorators import allowed_users, staff_or_admin_only
from domain.models.person import Person
from domain.forms.person import PersonForm, PersonUpdateForm


@login_required(login_url="user_login")
def person_list(request):
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request, "domain/persons.html", context)


@login_required(login_url="user_login")
@allowed_users(allowed_roles=["admin"])
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

            # create person object
            person = Person(
                id=uuid.uuid4(),
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                active=active,
                created=created,
                modified=modified,
            )
            # create user object and add to person.user
            user = User.objects.create_user(
                username=f"{person.first_name}{person.last_name}",
                email=person.email,
                password=form.cleaned_data["password"],
            )
            group = Group.objects.get(name="staff")
            user.groups.add(group)
            person.user = user
            person.save()
            messages.success(request, "Person is created successfully!")
            return redirect("persons")

    context = {"form": form}
    return render(request, "domain/person_create.html", context)


@login_required(login_url="user_login")
@staff_or_admin_only
def get_or_update_person_details(request, person_id: uuid.UUID):
    person = Person.objects.filter(id=person_id).first()
    if not person:
        raise Http404()

    user = person.user
    form = PersonUpdateForm(instance=person)
    is_staff = request.user.groups.filter(name="staff").exists()
    is_admin = request.user.groups.filter(name="admin").exists()

    if request.method == "POST":
        form = PersonUpdateForm(request.POST, instance=person)
        if form.is_valid():
            form.instance.modified = datetime.datetime.now()
            user.username = (
                f"{form.instance.first_name}{form.instance.last_name}"
            )
            user.email = form.instance.email
            user.save()
            form.save()
            messages.success(request, "Person is updated successfully!")
            return redirect("persons")

    context = {
        "form": form,
        "person": person,
        "is_staff": is_staff,
        "is_admin": is_admin,
        "can_edit": is_admin or (is_staff and request.user == person.user),
    }
    return render(request, "domain/person.html", context)


@login_required(login_url="user_login")
@allowed_users(allowed_roles=["admin"])
def delete_person(request, person_id: uuid.UUID):
    person = Person.objects.filter(id=person_id).first()
    if not person:
        raise Http404()

    if request.method == "POST":
        user = person.user
        person.delete()
        if user:
            user.delete()
        messages.success(request, "Person is deleted successfully!")
        return redirect("persons")

    context = {"person": person}
    return render(request, "domain/person_delete.html", context)

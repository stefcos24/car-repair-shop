from domain.models import Person


def person_context_processor(request):
    if request.user.is_authenticated:
        person = Person.objects.filter(user=request.user).first()
        return {"person": person}
    return {}

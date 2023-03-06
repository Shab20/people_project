from django.shortcuts import render
from django.views.generic import DetailView
from .models import Person


def people_list(request):
    people = Person.objects.order_by('age')
    return render(request, 'myapp/people_list.html', {'people': people})


class PersonDetailView(DetailView):
    model = Person

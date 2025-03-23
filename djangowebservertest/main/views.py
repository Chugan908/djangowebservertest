from random import *
import string

from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from main.models import City

# Create your views here.

def serialization_test(request):
    return JsonResponse({"message": "Hello, World!"}, safe=False)


def single_database_test(request):
    city = City.objects.get(id=randint(1, 4079))
    return JsonResponse(model_to_dict(city), safe=False)


def multiple_database_test(request):
    ids = [randint(1, 4079) for _ in range(5)]
    cities = [model_to_dict(city) for city in City.objects.filter(id__in=ids)]
    return JsonResponse(cities, safe=False)


def database_updates_view(request):
    results = []
    letters = string.ascii_lowercase

    for _ in range(5):
        new_name = ""
        city = City.objects.get(id=randint(1, 4079))

        for _ in range(randint(1, 35)):
            new_name += letters[randint(0, len(letters)-1)]

        city.name = new_name
        city.save()
        results.append({"id": city.id})

    return JsonResponse(results, safe=False)


def plaintext_view(request):
    response = HttpResponse(content="Hello, World!", content_type='text/plain')
    return response

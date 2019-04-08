from django.http import HttpResponse
from django.shortcuts import render
import yaml
import io

#


# Create your views here.
def index(request):
    with open("configuration_example.yaml", 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    context= {
        'data_loaded': data_loaded
    }

    weight =int(splitUnits(data_loaded.get('weight'))[0])

    if weight <= 10:
        data_loaded['image'] = data_loaded.get('image_light')
    elif weight <= 100:
        data_loaded['image'] = data_loaded.get('image_middle')
    else:
        data_loaded['image'] = data_loaded.get('image_heavy')

    return render(request, "units/index.html", context)

def splitUnits(givenString):
    return givenString.split(" ",  1)
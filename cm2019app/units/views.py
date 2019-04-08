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
    return render(request, "units/index.html", context)
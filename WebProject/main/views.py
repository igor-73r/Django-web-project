from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request, table=Total):
    fields_name = [f.name for f in table._meta.fields]
    fields = table._meta.get_fields()
    print(fields)
    query_results = table.objects.all()
    return render(request, 'main\index.html', locals())

def change_table(request):
    if 'Area' in request.POST:
        return index(request, Area)
    elif "Pos" in request.POST:
        return index(request, Position)
    elif "Type" in request.POST:
        return index(request, PrecipitationType)
    elif "Prec" in request.POST:
        return index(request, Precipitation)
    else:
        return index(request, Total)

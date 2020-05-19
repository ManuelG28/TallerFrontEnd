from django.shortcuts import render
from .forms import PredioForm
from . models import Predio
from django.http import HttpResponseRedirect
# Create your views here.
def predio_list(request):
    return render(request,"Predio/predioList.html")
def predio_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PredioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            predio = Predio()
            predio.latitud = form.cleaned_data["latitud"]
            predio.longitud = form.cleaned_data["longitud"]
            predio.terreno = form.cleaned_data["terreno"]
            predio.area = form.cleaned_data["area"]
            predio.value = 500
            predio.save()
            return HttpResponseRedirect('/predio/')

    return render(request,"Predio/predioForm.html")

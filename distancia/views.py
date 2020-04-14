from django.shortcuts import render
import requests
from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'distancia', 'value': value}
            response = requests.post('http://127.0.0.1:8000/distancia/', args)
            # Convierte la respuesta en JSON
            distancia_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/distancia/')
    # Convierte la respuesta en JSON
    distancias = response.json()
    # Rederiza la respuesta en el template measure
    print(distancias)
    return render(request, "distancia/distancia.html", {'distancias': distancias})
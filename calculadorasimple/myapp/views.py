from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    resultado = ''
    if request.method == 'POST':
        operador1 = float(request.POST.get('operador1'))
        operador2 = float(request.POST.get('operador2'))
        operacion = request.POST.get('operaciones')

        if operacion == 'suma':
            resultado = operador1 + operador2
        elif operacion == 'resta':
            resultado = operador1 - operador2
        elif operacion == 'multiplicacion':
            resultado = operador1 * operador2
        elif operacion == 'division':
            if operador2 != 0:
                resultado = operador1 / operador2
            else:
                resultado = 'Error: División por cero'
        else:
            resultado = 'Error: Operación no válida'

        # Redondear el resultado a un número entero si es necesario
        if isinstance(resultado, float):
            resultado = round(resultado)

    return render(request, 'index.html', {'resultado': resultado})
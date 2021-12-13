from django.shortcuts import render
from .models import Pizza, Topping


# Create your views here.
def index(request):
    return render(request, 'Pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date')

    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)
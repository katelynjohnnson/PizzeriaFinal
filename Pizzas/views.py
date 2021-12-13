from django.shortcuts import render, redirect
from .forms import PizzaForm
from .models import Pizza, Toppings


# Create your views here.
def index(request):
    return render(request, 'Pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date')

    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')
    
    context = {'pizza': pizza, 'toppings': toppings, 'comments': comments}
    return render(request, 'pizzas/pizza.html', context)


def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()

    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            form.save()

            return redirect('pizzas:pizzas')

    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html', context)

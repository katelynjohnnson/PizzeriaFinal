import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from Pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizzas in Pizza:
    print(pizzas.id)
    print(pizzas)
    print(pizzas.date)

p=Pizza.objects.get(id=1)
print(p)

toppings = p.entry_set.all()

for t in toppings:
    print(t)
from django.contrib import admin
from .models import Toppings
from .models import Comment

# Register your models here.
from .models import Pizza, Toppings

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Comment)
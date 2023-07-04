from django.contrib import admin
from .models import Country, State, City, Area, Branch, Service, Category, Item

# Register your models here.

admin.site.register([
    Country,
    State,
    City,
    Area,
    Branch,
    Service,
    Category,
    Item
])
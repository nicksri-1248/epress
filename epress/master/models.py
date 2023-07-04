from django.db import models
from loginapp.models import User
from django.utils import timezone

#COUNTRY

class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)
    currency = models.CharField(max_length=50, blank=False, null=False)
    currency_symbol = models.CharField(max_length=10, blank=False, null=False)
    language = models.CharField(max_length=50, blank=False, null=False)
    language_code = models.CharField(max_length=10, blank=False, null=False)
    flag = models.CharField(max_length=10, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        self.currency = self.currency.upper()
        #self.currency_symbol = self.currency_symbol.upper()
        self.language = self.language.upper()
        self.language_code = self.language_code.upper()
        self.flag = self.flag.upper()
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#COUNTRY

#STATE

class State(models.Model):
    COUNTRY_CHOICES = [(country.name, country.name) for country in Country.objects.all()]

    country = models.CharField(max_length=255, blank=False, choices=COUNTRY_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)
    language = models.CharField(max_length=50, blank=False, null=False)
    language_code = models.CharField(max_length=10, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        self.language = self.language.upper()
        self.language_code = self.language_code.upper()
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#STATE

#CITY

class City(models.Model):
    COUNTRY_CHOICES = [(country.name, country.name) for country in Country.objects.all()]
    STATE_CHOICES = [(state.name, state.name) for state in State.objects.all()]

    country = models.CharField(max_length=255, blank=False, choices=COUNTRY_CHOICES)
    state = models.CharField(max_length=255, blank=False, choices=STATE_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#AREA

class Area(models.Model):
    CITY_CHOICES = [(city.name, city.name) for city in City.objects.all()]

    city = models.CharField(max_length=255, blank=False, choices=CITY_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.IntegerField(blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        #self.code = self.code.upper()
        super(Area, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#AREA

#BRANCH

class Branch(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()
        super(Branch, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#BRANCH

#SERVICE

class Service(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#SERVICE

#CATEGORY

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#CATEGORY

#ITEM

class Item(models.Model):
    SERVICE_CHOICES = [(service.name, service.name) for service in Service.objects.all()]
    CATEGORY_CHOICES = [(category.name, category.name) for category in Category.objects.all()]

    service = models.CharField(max_length=255, blank=False, choices=SERVICE_CHOICES)
    category = models.CharField(max_length=255, blank=False, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#ITEM

'''#ORDER

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

#ORDER'''
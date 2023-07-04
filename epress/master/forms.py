from django import forms
from .models import Country, State, City, Area, Branch, Service, Category, Item

#COUNTRY

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'code', 'currency', 'currency_symbol', 'language', 'language_code', 'flag']
        labels = {
            'name': 'Country Name',
            'code': 'Country Code',
            'currency': 'Currency',
            'currency_symbol': 'Currency Symbol',
            'language': 'Language',
            'language_code': 'Language Code',
            'flag': 'Flag',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.TextInput(attrs={'class': 'form-control'}),
            'currency_symbol': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'language_code': forms.TextInput(attrs={'class': 'form-control'}),
            'flag': forms.TextInput(attrs={'class': 'form-control'}),
        }

#COUNTRY

#STATE

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ['country', 'name', 'code', 'language', 'language_code']
        labels = {
            'country': 'Country',
            'name': 'State Name',
            'code': 'State Code',
            'language': 'Language',
            'language_code': 'Language Code',
        }
        widgets = {
            'country': forms.Select(choices=State.COUNTRY_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'language_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

#STATE

#CITY

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ['country', 'state', 'name', 'code']
        labels = {
            'country': 'Country',
            'state': 'State',
            'name': 'City Name',
            'code': 'City Code',
        }
        widgets = {
            'country': forms.Select(choices=City.COUNTRY_CHOICES, attrs={'class': 'form-control'}),
            'state': forms.Select(choices=City.STATE_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }

#CITY

#AREA

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['city', 'name', 'code']
        labels = {
            'city': 'City',
            'name': 'Area Name',
            'code': 'PinCode',
        }
        widgets = {
            'city': forms.Select(choices=Area.CITY_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }

#AREA

#BRANCH

class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ['name', 'code', 'address']
        labels = {
            'name': 'Branch Name',
            'code': 'Branch Code',
            'address': 'Address',
        }
        widgets = {
            #'city': forms.Select(choices=Area.CITY_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

#BRANCH

#SERVICE

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'description']
        labels = {
            'name': 'Service Name',
            'description': 'Description'
        }
        widgets = {
            #'city': forms.Select(choices=Area.CITY_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 40}),
        }

#SERVICE

#CATEGORY

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

#CATEGORY

#ITEM

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['service', 'category', 'name', 'price']
        labels = {
            'service': 'Service',
            'category': 'Category',
            'name': 'Item Name',
            'price': 'Price',
        }
        widgets = {
            'service': forms.Select(choices=Item.SERVICE_CHOICES, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Item.CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }

#ITEM
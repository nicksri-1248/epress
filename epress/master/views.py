import uuid
import time
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Country, State, City, Area, Branch, Service, Category, Item#, Order
from .forms import CountryForm, StateForm, CityForm, AreaForm, BranchForm, ServiceForm, CategoryForm, ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Max

#COUNTRY

class CountryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Country
    template_name = 'master/country/country_list.html'
    context_object_name = 'countries'

    def test_func(self):
        return self.request.user.is_superuser

class CountryAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = CountryForm()
        return render(request, 'master/country/country_edit.html', {'form': form, 'title': 'Add country'})

    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        return render(request, 'master/country/country_edit.html', {'form': form, 'title': 'Add country'})

class CountryEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        form = CountryForm(instance=country)
        return render(request, 'master/country/country_edit.html', {'form': form, 'title': 'Edit country'})

    def post(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_detail', pk=pk)
        return render(request, 'master/country/country_edit.html', {'form': form, 'title': 'Edit country'})

class CountryDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        return render(request, 'master/country/country_delete.html', {'country': country})

    def post(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        country.delete()
        return redirect('country_list')

class CountryDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        return render(request, 'master/country/country_detail.html', {'country': country})

#COUNTRY

#STATE

class StateListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = State
    template_name = 'master/state/state_list.html'
    context_object_name = 'states'

    def test_func(self):
        return self.request.user.is_superuser

class StateAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = StateForm()
        return render(request, 'master/state/state_edit.html', {'form': form, 'title': 'Add state'})

    def post(self, request):
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_list')
        return render(request, 'master/state/state_edit.html', {'form': form, 'title': 'Add state'})

class StateEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        state = get_object_or_404(State, pk=pk)
        form = StateForm(instance=state)
        return render(request, 'master/state/state_edit.html', {'form': form, 'title': 'Edit state'})

    def post(self, request, pk):
        state = get_object_or_404(State, pk=pk)
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_detail', pk=pk)
        return render(request, 'master/state/state_edit.html', {'form': form, 'title': 'Edit state'})

class StateDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        state = get_object_or_404(State, pk=pk)
        return render(request, 'master/state/state_delete.html', {'state': state})

    def post(self, request, pk):
        state = get_object_or_404(State, pk=pk)
        state.delete()
        return redirect('state_list')

class StateDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        state = get_object_or_404(State, pk=pk)
        return render(request, 'master/state/state_detail.html', {'state': state})

#STATE

#CITY

class CityListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = City
    template_name = 'master/city/city_list.html'
    context_object_name = 'cities'

    def test_func(self):
        return self.request.user.is_superuser

class CityAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = CityForm()
        return render(request, 'master/city/city_edit.html', {'form': form, 'title': 'Add city'})

    def post(self, request):
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')
        return render(request, 'master/city/city_edit.html', {'form': form, 'title': 'Add city'})

class CityEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        form = CityForm(instance=city)
        return render(request, 'master/city/city_edit.html', {'form': form, 'title': 'Edit city'})

    def post(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city_detail', pk=pk)
        return render(request, 'master/city/city_edit.html', {'form': form, 'title': 'Edit city'})

class CityDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        return render(request, 'master/city/city_delete.html', {'city': city})

    def post(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        city.delete()
        return redirect('city_list')

class CityDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        return render(request, 'master/city/city_detail.html', {'city': city})

class CityAreaView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'master/city/city_area.html'
    context_object_name = 'areas'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        city = get_object_or_404(City, name=city_name)
        queryset = Area.objects.filter(city=city)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_name = self.kwargs['city_name']
        city = get_object_or_404(City, name=city_name)
        context['city'] = city
        return context



#CITY

#AREA

class AreaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Area
    template_name = 'master/area/area_list.html'
    context_object_name = 'areas'

    def test_func(self):
        return self.request.user.is_superuser

class AreaAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = AreaForm()
        return render(request, 'master/area/area_edit.html', {'form': form, 'title': 'Add area'})

    def post(self, request):
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_list')
        return render(request, 'master/area/area_edit.html', {'form': form, 'title': 'Add area'})

class AreaEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        area = get_object_or_404(Area, pk=pk)
        form = AreaForm(instance=area)
        return render(request, 'master/area/area_edit.html', {'form': form, 'title': 'Edit area'})

    def post(self, request, pk):
        area = get_object_or_404(Area, pk=pk)
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('area_detail', pk=pk)
        return render(request, 'master/area/area_edit.html', {'form': form, 'title': 'Edit area'})

class AreaDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        area = get_object_or_404(Area, pk=pk)
        return render(request, 'master/area/area_delete.html', {'area': area})

    def post(self, request, pk):
        area = get_object_or_404(Area, pk=pk)
        area.delete()
        return redirect('area_list')

class AreaDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        area = get_object_or_404(Area, pk=pk)
        return render(request, 'master/area/area_detail.html', {'area': area})

#AREA

#BRANCH

class BranchListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Branch
    template_name = 'master/branch/branch_list.html'
    context_object_name = 'branches'

    def test_func(self):
        return self.request.user.is_superuser

class BranchAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = BranchForm()
        return render(request, 'master/branch/branch_edit.html', {'form': form, 'title': 'Add branch'})

    def post(self, request):
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
        return render(request, 'master/branch/branch_edit.html', {'form': form, 'title': 'Add branch'})

class BranchEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        form = BranchForm(instance=branch)
        return render(request, 'master/branch/branch_edit.html', {'form': form, 'title': 'Edit branch'})

    def post(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_detail', pk=pk)
        return render(request, 'master/branch/branch_edit.html', {'form': form, 'title': 'Edit branch'})

class BranchDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        return render(request, 'master/branch/branch_delete.html', {'branch': branch})

    def post(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
        return redirect('branch_list')

class BranchDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        branch = get_object_or_404(Branch, pk=pk)
        return render(request, 'master/branch/branch_detail.html', {'branch': branch})

#BRANCH

#SERVICE

class ServiceListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Service
    template_name = 'master/service/service_list.html'
    context_object_name = 'services'

    def test_func(self):
        return self.request.user.is_superuser

class ServiceAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = ServiceForm()
        return render(request, 'master/service/service_edit.html', {'form': form, 'title': 'Add service'})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        return render(request, 'master/service/service_edit.html', {'form': form, 'title': 'Add service'})

class ServiceEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(instance=service)
        return render(request, 'master/service/service_edit.html', {'form': form, 'title': 'Edit service'})

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', pk=pk)
        return render(request, 'master/service/service_edit.html', {'form': form, 'title': 'Edit service'})

class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        return render(request, 'master/service/service_delete.html', {'service': service})

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        return redirect('service_list')

class ServiceDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        return render(request, 'master/service/service_detail.html', {'service': service})

#SERVICE

#CATEGORY

class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    template_name = 'master/category/category_list.html'
    context_object_name = 'categories'

    def test_func(self):
        return self.request.user.is_superuser

class CategoryAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = CategoryForm()
        return render(request, 'master/category/category_edit.html', {'form': form, 'title': 'Add category'})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        return render(request, 'master/category/category_edit.html', {'form': form, 'title': 'Add category'})

class CategoryEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'master/category/category_edit.html', {'form': form, 'title': 'Edit category'})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=pk)
        return render(request, 'master/category/category_edit.html', {'form': form, 'title': 'Edit category'})

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'master/category/category_delete.html', {'category': category})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('category_list')

class CategoryDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'master/category/category_detail.html', {'category': category})

#CATEGORY

#ITEM

class ItemListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Item
    template_name = 'master/item/item_list.html'
    context_object_name = 'items'

    def test_func(self):
        return self.request.user.is_superuser

class ItemAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = ItemForm()
        return render(request, 'master/item/item_edit.html', {'form': form, 'title': 'Add item'})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'master/item/item_edit.html', {'form': form, 'title': 'Add item'})

class ItemEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(instance=item)
        return render(request, 'master/item/item_edit.html', {'form': form, 'title': 'Edit item'})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=pk)
        return render(request, 'master/item/item_edit.html', {'form': form, 'title': 'Edit item'})

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'master/item/item_delete.html', {'item': item})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('item_list')

class ItemDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'master/item/item_detail.html', {'item': item})

#ITEM


'''
#ORDER

class OrderListView(LoginRequiredMixin, View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'master/order/item_order_list.html', {'items': items})

    def post(self, request):
        order_number = int(time.time() * 1000) + random.randint(1, 1000)

        item_ids = request.POST.getlist('item_id')
        quantities = request.POST.getlist('item')
        for item_id, quantity in zip(item_ids, quantities):
            if int(quantity) > 0:
                order = Order(item_id=item_id, quantity=quantity, order_number=order_number)
                order.user = request.user
                order.save()
        return render(request, 'master/order/item_order_list.html', {'items': Item.objects.all()})


class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        order = Order.objects.all().values('order_number').distinct()
        order = order.filter(user=self.request.user)
        return render(request, 'master/order/order_history.html', {'order': order})



class OrderDetailView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'master/order/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        order_number = self.kwargs['order_number']
        return Order.objects.filter(order_number=order_number, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_number'] = self.kwargs['order_number']
        return context

#ORDER

'''
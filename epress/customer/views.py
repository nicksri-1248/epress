from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from loginapp.models import User
from django.views.generic import ListView
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#CUSTOMER

class CustomerListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'customer/customer_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

'''class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'

class CustomerAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customer/customer_edit.html', {'form': form, 'title': 'Add customer'})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer/customer_edit.html', {'form': form, 'title': 'Add customer'})

class CustomerEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, 'customer/customer_edit.html', {'form': form, 'title': 'Edit customer'})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=pk)
        return render(request, 'customer/customer_edit.html', {'form': form, 'title': 'Edit customer'})

class CustomerDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customer/customer_delete.html', {'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')

class CustomerDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customer/customer_detail.html', {'customer': customer})'''

#CUSTOMER

'''#ADDRESS

class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'customer/address/address_list.html'
    context_object_name = 'addresses'

class AddressAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'customer/address/address_edit.html', {'form': form, 'title': 'Add address'})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_list')
        return render(request, 'customer/address/address_edit.html', {'form': form, 'title': 'Add address'})

class AddressEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        form = AddressForm(instance=address)
        return render(request, 'customer/address/address_edit.html', {'form': form, 'title': 'Edit address'})

    def post(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_detail', pk=pk)
        return render(request, 'customer/address/address_edit.html', {'form': form, 'title': 'Edit address'})

class AddressDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        return render(request, 'customer/address/address_delete.html', {'address': address})

    def post(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        address.delete()
        return redirect('address_list')

class AddressDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        return render(request, 'customer/address/address_detail.html', {'address': address})

#ADDRESS'''
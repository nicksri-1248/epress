'''import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Address
from .forms import AddressForm
from django.contrib.auth.mixins import LoginRequiredMixin'''

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Address
from .forms import AddressForm

class AddAddressView(LoginRequiredMixin, View):
    template_name = 'address/add_address.html'
    form_class = AddressForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address_list')
        return render(request, self.template_name, {'form': form})


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'address/address_list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset



'''class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'addressbook/address_list.html'
    context_object_name = 'addresses'

class AddressAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'addressbook/address_edit.html', {'form': form, 'title': 'Add address'})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_list')
        return render(request, 'addressbook/address_edit.html', {'form': form, 'title': 'Add address'})

class AddressEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        form = AddressForm(instance=address)
        return render(request, 'addressbook/address_edit.html', {'form': form, 'title': 'Edit address'})

    def post(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_detail', pk=pk)
        return render(request, 'addressbook/address_edit.html', {'form': form, 'title': 'Edit address'})

class AddressDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        return render(request, 'addressbook/address_delete.html', {'address': address})

    def post(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        address.delete()
        return redirect('address_list')

class AddressDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        address = get_object_or_404(Address, pk=pk)
        return render(request, 'addressbook/address_detail.html', {'address': address})'''
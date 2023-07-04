import uuid
import time
import random
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic import ListView
from master.models import Item, Service
from .models import Order, Address
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AddressForm
from django.http import HttpResponse
from django.db.models import Count

#ADDRESS

class AddAddressView(LoginRequiredMixin, View):
    template_name = 'dashboard/address/add_address.html'
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
    template_name = 'dashboard/address/address_list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

#ADDRESS

#ORDER

class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'dashboard/order/service_list.html'
    context_object_name = 'services'

'''class ServiceListView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'dashboard/order/service_list.html', {'services': services})'''

class OrderListView(LoginRequiredMixin, View):
    '''model = Item
    template_name = 'dashboard/order/item_order_list.html.html'
    context_object_name = 'items'

    def get_queryset(self):
        service = self.kwargs['service']
        return Order.objects.filter(service=service, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.kwargs['service']
        return context'''


    def get(self, request, service_name):
        service = Service.objects.get(name=service_name)
        items = Item.objects.filter(service=service)
        return render(request, 'dashboard/order/item_order_list.html', {'items': items})

    def post(self, request, service_name):
        order_number = int(time.time() * 1000) + random.randint(1, 1000)

        item_ids = request.POST.getlist('item_id')
        quantities = request.POST.getlist('item')
        for item_id, quantity in zip(item_ids, quantities):
            if int(quantity) > 0:
                order = Order(item_id=item_id, quantity=quantity, order_number=order_number)
                order.user = request.user
                order.save()
        addresses = Order.objects.all().values('address').distinct()
        if addresses.exists():
            return redirect('select_address', order_number=order_number)
        else:
            return redirect('name_and_address', order_number=order_number)

class NameAndAddressView(LoginRequiredMixin, View):
    def get(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        return render(request, 'dashboard/order/name_and_address.html', {'orders': orders})

    def post(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        for order in orders:
            #order.name = request.POST.get('name')
            order.address = request.POST.get('address')
            order.user = request.user
            order.save()
        return redirect('delivery_date_and_time', order.order_number)

class SelectAddressView(View):
    def get(self, request, order_number):
        addresses = Order.objects.values('address').annotate(num_orders=Count('id')).filter(num_orders__gt=0)
        return render(request, 'dashboard/order/select_address.html', {'addresses': addresses, 'order_number': order_number})

    def post(self, request, order_number):
        selected_address = request.POST.get('selected_address')
        if 'name_and_address' in request.POST:
            return redirect('name_and_address', order_number=order_number)
        else:
            orders = Order.objects.filter(order_number=order_number)
            for order in orders:
                order.address = selected_address
                order.user = request.user
                order.save()
            return redirect('delivery_date_and_time', order_number=order_number)



class DeliveryDateAndTimeView(LoginRequiredMixin, View):
    def get(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        return render(request, 'dashboard/order/delivery_date_and_time.html', {'orders': orders})

    def post(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        for order in orders:
            order.delivery_date = request.POST.get('delivery_date')
            order.delivery_time = request.POST.get('delivery_time')
            order.user = request.user
            order.save()
        return redirect('payment', order.order_number)


class PaymentView(LoginRequiredMixin, View):
    def get(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        return render(request, 'dashboard/order/payment.html', {'orders': orders})

    def post(self, request, order_number):
        orders = Order.objects.filter(order_number=order_number)
        for order in orders:
        # Add payment processing code here
            order.payment_status = True
            order.user = request.user
            order.save()
        return HttpResponse('Payment Successful')

class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.all().values('order_number').distinct()
        orders = orders.filter(user=self.request.user)
        return render(request, 'dashboard/order/order_history.html', {'orders': orders})

class OrderDetailView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/order/order_detail.html'
    context_object_name = 'orders'

    def get_queryset(self):
        order_number = self.kwargs['order_number']
        return Order.objects.filter(order_number=order_number, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_number'] = self.kwargs['order_number']
        return context

#ORDER
from django.urls import path
from .views import OrderListView, OrderHistoryView, OrderDetailView, AddAddressView, AddressListView, NameAndAddressView, SelectAddressView, DeliveryDateAndTimeView, PaymentView, ServiceListView

urlpatterns = [
    path('order/', ServiceListView.as_view(), name='order_service_list'),
    path('order/<str:service_name>/', OrderListView.as_view(), name='order_list'),
    #path('item/', OrderListView.as_view(), name='order_list'),
    path('name-and-address/<int:order_number>/', NameAndAddressView.as_view(), name='name_and_address'),
    path('select-address/<int:order_number>/', SelectAddressView.as_view(), name='select_address'),
    path('delivery-date-and-time/<int:order_number>/', DeliveryDateAndTimeView.as_view(), name='delivery_date_and_time'),
    path('payment/<int:order_number>/', PaymentView.as_view(), name='payment'),
    path('orders/', OrderHistoryView.as_view(), name='order_history'),
    path('order/<str:order_number>/', OrderDetailView.as_view(), name='order_detail'),
    path('add/', AddAddressView.as_view(), name='add_address'),
    path('', AddressListView.as_view(), name='address_list'),
]
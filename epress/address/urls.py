'''from django.urls import path
from .views import AddressListView, AddressAddView, AddressEditView, AddressDeleteView, AddressDetailView

urlpatterns = [
    path('address/', AddressListView.as_view(), name='address_list'),
    path('address/add/', AddressAddView.as_view(), name='address_add'),
    path('address/<int:pk>/edit/', AddressEditView.as_view(), name='address_edit'),
    path('address/<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),
    path('address/<int:pk>/', AddressDetailView.as_view(), name='address_detail'),
]'''
from django.urls import path
from .views import AddAddressView, AddressListView

urlpatterns = [
    path('add/', AddAddressView.as_view(), name='add_address'),
    path('', AddressListView.as_view(), name='address_list'),
]

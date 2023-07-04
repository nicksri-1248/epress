from django.urls import path
from .views import CustomerListView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    #path('add/', CustomerAddView.as_view(), name='customer_add'),
    #path('<int:pk>/edit/', CustomerEditView.as_view(), name='customer_edit'),
    #path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    #path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
]
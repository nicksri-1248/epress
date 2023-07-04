from django.urls import path
from .views import CountryListView, CountryAddView, CountryEditView, CountryDeleteView, CountryDetailView
from .views import StateListView, StateAddView, StateEditView, StateDeleteView, StateDetailView
from .views import CityListView, CityAddView, CityEditView, CityDeleteView, CityDetailView, CityAreaView
from .views import AreaListView, AreaAddView, AreaEditView, AreaDeleteView, AreaDetailView
from .views import BranchListView, BranchAddView, BranchEditView, BranchDeleteView, BranchDetailView
from .views import ServiceListView, ServiceAddView, ServiceEditView, ServiceDeleteView, ServiceDetailView
from .views import CategoryListView, CategoryAddView, CategoryEditView, CategoryDeleteView, CategoryDetailView
from .views import ItemListView, ItemAddView, ItemEditView, ItemDeleteView, ItemDetailView

urlpatterns = [
    path('country/', CountryListView.as_view(), name='country_list'),
    path('country/add/', CountryAddView.as_view(), name='country_add'),
    path('country/<int:pk>/edit/', CountryEditView.as_view(), name='country_edit'),
    path('country/<int:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('state/', StateListView.as_view(), name='state_list'),
    path('state/add/', StateAddView.as_view(), name='state_add'),
    path('state/<int:pk>/edit/', StateEditView.as_view(), name='state_edit'),
    path('state/<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
    path('state/<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('area_list/<str:city_name>/', CityAreaView.as_view(), name='city_area'),
    path('city/', CityListView.as_view(), name='city_list'),
    path('city/add/', CityAddView.as_view(), name='city_add'),
    path('city/<int:pk>/edit/', CityEditView.as_view(), name='city_edit'),
    path('city/<int:pk>/delete/', CityDeleteView.as_view(), name='city_delete'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('area/', AreaListView.as_view(), name='area_list'),
    path('area/add/', AreaAddView.as_view(), name='area_add'),
    path('area/<int:pk>/edit/', AreaEditView.as_view(), name='area_edit'),
    path('area/<int:pk>/delete/', AreaDeleteView.as_view(), name='area_delete'),
    path('area/<int:pk>/', AreaDetailView.as_view(), name='area_detail'),
    path('branch/', BranchListView.as_view(), name='branch_list'),
    path('branch/add/', BranchAddView.as_view(), name='branch_add'),
    path('branch/<int:pk>/edit/', BranchEditView.as_view(), name='branch_edit'),
    path('branch/<int:pk>/delete/', BranchDeleteView.as_view(), name='branch_delete'),
    path('branch/<int:pk>/', BranchDetailView.as_view(), name='branch_detail'),
    path('service/', ServiceListView.as_view(), name='service_list'),
    path('service/add/', ServiceAddView.as_view(), name='service_add'),
    path('service/<int:pk>/edit/', ServiceEditView.as_view(), name='service_edit'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryAddView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', CategoryEditView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('item/', ItemListView.as_view(), name='item_list'),
    path('item/add/', ItemAddView.as_view(), name='item_add'),
    path('item/<int:pk>/edit/', ItemEditView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail')
]
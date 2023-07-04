from django.urls import path
from .views import QueryListView, QueryAddView, QueryEditView, QueryDeleteView, QueryDetailView

urlpatterns = [
    path('', QueryListView.as_view(), name='query_list'),
    path('add/', QueryAddView.as_view(), name='query_add'),
    path('<int:pk>/edit/', QueryEditView.as_view(), name='query_edit'),
    path('<int:pk>/delete/', QueryDeleteView.as_view(), name='query_delete'),
    path('<int:pk>/', QueryDetailView.as_view(), name='query_detail'),
]
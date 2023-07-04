
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Query
from .forms import QueryForm


class QueryListView(ListView):
    model = Query
    template_name = 'query/query_list.html'
    context_object_name = 'queries'

    def test_func(self):
        return self.request.user.is_superuser


class QueryAddView(View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = QueryForm()
        return render(request, 'query/query_edit.html', {'form': form, 'title': 'Add query'})

    def post(self, request):
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_list')
        return render(request, 'query/query_edit.html', {'form': form, 'title': 'Add query'})


class QueryEditView(View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        query = get_object_or_404(Query, pk=pk)
        form = QueryForm(instance=query)
        return render(request, 'query/query_edit.html', {'form': form, 'title': 'Edit query'})

    def post(self, request, pk):
        query = get_object_or_404(Query, pk=pk)
        form = QueryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('query_detail', pk=pk)
        return render(request, 'query/query_edit.html', {'form': form, 'title': 'Edit query'})


class QueryDeleteView(View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        query = get_object_or_404(Query, pk=pk)
        return render(request, 'query/query_delete.html', {'query': query})

    def post(self, request, pk):
        query = get_object_or_404(Query, pk=pk)
        query.delete()
        return redirect('query_list')


class QueryDetailView(View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        query = get_object_or_404(Query, pk=pk)
        return render(request, 'query/query_detail.html', {'query': query})



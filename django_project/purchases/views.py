from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from purchases.models import Purchase


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchases/purchase_list.html'

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchases/purchase_detail.html'
    context_object_name = 'purchase'

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchases/purchase_create.html'
    fields = ('user', 'book',)
    success_url = reverse_lazy('purchases:purchase-list')


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = 'purchases/purchase_update.html'
    context_object_name = 'purchase'
    fields = ('user', 'book',)
    success_url = reverse_lazy('purchases:purchase-list')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'purchases/purchase_delete.html'
    success_url = reverse_lazy('purchases:purchase-list')
    context_object_name = 'purchase'

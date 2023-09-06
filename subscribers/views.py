from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Subscribers

# Create your views here.


class SubscribersListView(ListView):
    model = Subscribers
    field = ['email', 'first_name', 'is_active']
    template_name = 'subscribers/list.html'
    context_object_name = 'subscribers_list'

    def get_queryset(self):
        return Subscribers.objects.all()


class SubscribersCreateView(CreateView):
    model = Subscribers
    fields = ['email', 'first_name']
    template_name = 'subscribers/add.html'
    success_url = '/subscribers/list/'


class SubscribersUpdateView(UpdateView):
    model = Subscribers
    fields = ['email', 'first_name', 'is_active']
    template_name = 'subscribers/add.html'
    success_url = '/subscribers/list/'


class SubscriberDeleteView(DeleteView):
    model = Subscribers
    template_name = 'subscribers/delete.html'
    success_url = '/subscribers/list/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['subscriber'] = self.get_object()
        return context

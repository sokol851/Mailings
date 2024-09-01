from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import ClientForm
from mailings.models import Client


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class ClientDetailView(DetailView):
    model = Client

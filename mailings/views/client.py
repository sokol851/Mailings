from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import ClientForm
from mailings.models import Client


class ClientListView(ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(creator=self.request.user)
        return queryset


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        user = form.save()
        if user.first_name == '' or user.first_name is None:
            user.first_name = 'Не указано'
        if user.last_name == '' or user.last_name is None:
            user.last_name = 'Не указано'
        if user.patronymic == '' or user.patronymic is None:
            user.patronymic = 'Не указано'
        if user.comment == '' or user.comment is None:
            user.comment = 'Не указано'
        user.save()
        return super().form_valid(form)


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class ClientDetailView(DetailView):
    model = Client

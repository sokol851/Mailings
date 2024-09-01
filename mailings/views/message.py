from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import MessageForm
from mailings.models import Message


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class MessageDetailView(DetailView):
    model = Message

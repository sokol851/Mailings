from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import MailingSettingsForm
from mailings.models import MailingSettings


class MessageListView(ListView):
    model = MailingSettings


class MessageUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')


class MessageCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')


class MessageDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')


class MessageDetailView(DetailView):
    model = MailingSettings

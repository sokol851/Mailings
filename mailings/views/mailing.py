from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import MailingSettingsForm
from mailings.models import MailingSettings


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser or user.has_perm('mailings.view_all_list'):
            queryset = MailingSettings.objects.all()
        else:
            queryset = queryset.filter(creator=user)
        return queryset


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')

    def get_form_kwargs(self):
        kwargs = super(MailingSettingsUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MailingSettingsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')


class MailingSettingsDetailView(DetailView):
    model = MailingSettings

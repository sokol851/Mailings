from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from mailings.forms import MailingSettingsForm
from mailings.models import MailingSettings


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser or user.has_perm('mailings.view_all_list'):
            queryset = MailingSettings.objects.all()
        else:
            queryset = queryset.filter(creator=user)
        return queryset


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')

    def get_form_kwargs(self):
        kwargs = super(MailingSettingsUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.creator or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied

    @staticmethod
    def edit_status(request, pk):
        mailing_items = get_object_or_404(MailingSettings, pk=pk)
        if mailing_items.status == MailingSettings.CREATED or mailing_items.status == MailingSettings.WORKS:
            mailing_items.status = MailingSettings.FINISHED
        else:
            mailing_items.status = MailingSettings.WORKS
        mailing_items.save()
        return redirect(reverse('mailings:mailing_list'))


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
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


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.creator or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings

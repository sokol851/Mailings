from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from mailings.models import MailingLog


class MailingLogListView(LoginRequiredMixin, ListView):
    model = MailingLog

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(creator=self.request.user).order_by('last_attempt')
        return queryset

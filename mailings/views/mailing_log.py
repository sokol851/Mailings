from django.views.generic import ListView

from mailings.models import MailingLog


class MailingLogListView(ListView):
    model = MailingLog

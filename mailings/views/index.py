from django.shortcuts import render
from django.views.generic import TemplateView

from mailings.models import MailingSettings, Client


class Index(TemplateView):
    """
    Контроллер главной страницы сайта
    """
    template_name = 'mailings/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Проверяем аутентификацию
        if self.request.user.is_authenticated:
            # Получение личной статистики
            mailings = MailingSettings.objects.all()
            clients = Client.objects.all()
            context_data['full_all_mailings'] = mailings.count()
            count_mailings_works_all = mailings.filter(status=MailingSettings.WORKS).count()
            count_mailings_created_all = mailings.filter(status=MailingSettings.CREATED).count()
            context_data['full_active_mailings'] = count_mailings_works_all + count_mailings_created_all
            context_data['full_active_clients'] = clients.values('email').distinct().count()

            # Получение общей статистики
            context_data['all_mailings'] = mailings.filter(creator=self.request.user).count()
            count_mailings_works = mailings.filter(creator=self.request.user).filter(
                status=MailingSettings.WORKS).count()
            count_mailings_created = mailings.filter(creator=self.request.user).filter(
                status=MailingSettings.CREATED).count()
            context_data['active_mailings'] = count_mailings_works + count_mailings_created
            context_data['active_clients'] = clients.values('email').distinct().filter(
                creator=self.request.user).count()
        return context_data

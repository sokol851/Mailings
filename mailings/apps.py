from time import sleep

from django.apps import AppConfig

from config.settings import DEFAULT_AUTO_FIELD


class MailingsConfig(AppConfig):
    default_auto_field = DEFAULT_AUTO_FIELD
    verbose_name = 'Рассылка'
    name = 'mailings'

    def ready(self):
        from mailings.services import service_send_mails
        sleep(2)
        service_send_mails()

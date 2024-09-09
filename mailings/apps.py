from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

from config.settings import DEFAULT_AUTO_FIELD


class MailingsConfig(AppConfig):
    default_auto_field = DEFAULT_AUTO_FIELD
    verbose_name = 'Рассылка'
    name = 'mailings'

    def ready(self):
        scheduler = BackgroundScheduler()
        from mailings.services import service_send_mails
        if not scheduler.get_jobs():
            scheduler.add_job(service_send_mails, 'interval', seconds=10)
        if not scheduler.running:
            scheduler.start()

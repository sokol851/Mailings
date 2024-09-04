from django.core.management import BaseCommand

from mailings.services import service_send_mails


class Command(BaseCommand):
    def handle(self, *args, **options):
        service_send_mails()

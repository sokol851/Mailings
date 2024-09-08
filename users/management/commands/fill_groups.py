from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from mailings.models import MailingSettings
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Создаем группу модераторов
        moderator_group, created = Group.objects.get_or_create(name='Moderator')

        # Определяем тип контента для модели рассылки
        content_type_mailings = ContentType.objects.get_for_model(MailingSettings)
        content_type_user = ContentType.objects.get_for_model(User)

        # Определяем и создаем необходимые права, если они не существуют
        permissions = [
            Permission.objects.get_or_create(
                codename='view_all_list',
                name='view all list',
                content_type=content_type_mailings
            )[0],
            Permission.objects.get_or_create(
                codename='view_all_user',
                name='view all user',
                content_type=content_type_user
            )[0],
            Permission.objects.get_or_create(
                codename='ban_user',
                name='ban user',
                content_type=content_type_user
            )[0],
            Permission.objects.get_or_create(
                codename='Disabled_mailing',
                name='Disabled mailing',
                content_type=content_type_mailings
            )[0],
        ]

        # Назначаем права группе
        for permission in permissions:
            moderator_group.permissions.add(permission)

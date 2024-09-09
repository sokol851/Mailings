from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from blog.models import Blog
from mailings.models import MailingSettings, Client, Message
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Создаем группу модераторов
        moderator_group, created = Group.objects.get_or_create(name='Manager')

        # Определяем тип контента для модели рассылки
        content_type_mailings = ContentType.objects.get_for_model(MailingSettings)
        content_type_user = ContentType.objects.get_for_model(User)
        content_type_blog = ContentType.objects.get_for_model(Blog)
        content_type_client = ContentType.objects.get_for_model(Client)
        content_type_message = ContentType.objects.get_for_model(Message)

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
            Permission.objects.get(codename='add_blog'),
            Permission.objects.get(codename='change_blog'),
            Permission.objects.get(codename='delete_blog'),
            Permission.objects.get(codename='view_blog'),
            Permission.objects.get(codename='view_client'),
            Permission.objects.get(codename='view_mailingsettings'),
            Permission.objects.get(codename='view_message'),
        ]

        # Назначаем права группе
        for permission in permissions:
            moderator_group.permissions.add(permission)

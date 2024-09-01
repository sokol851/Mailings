from django.contrib import admin

from mailings.models import Client, Message, MailingSettings, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'patronymic', 'comment',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'body',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_at', 'stop_at', 'periodicity', 'status', 'message',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status_attempt', 'response', 'mailing',)

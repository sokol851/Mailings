from datetime import datetime, timedelta

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта клиента')
    first_name = models.CharField(max_length=100, **NULLABLE, default='Не указано', verbose_name='Имя')
    last_name = models.CharField(max_length=100, **NULLABLE, default='Не указано', verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, **NULLABLE, default='Не указано', verbose_name='Отчество')
    comment = models.CharField(max_length=50, **NULLABLE, default='Не указано', verbose_name='Комментарий')
    creator = models.ForeignKey(User, max_length=150, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Создатель')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    creator = models.ForeignKey(User, max_length=150, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Создатель')

    def __str__(self):
        return f'{self.theme}: {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    EVERY_DAY = 'EVERY_DAY'
    EVERY_WEEK = 'EVERY_WEEK'
    EVERY_MONTH = 'EVERY_MONTH'

    PERIODICITY_SET = ((EVERY_DAY, 'Каждый день'), (EVERY_WEEK, 'Каждую неделю'), (EVERY_MONTH, 'каждый месяц'))

    CREATED = 'Создана'
    WORKS = 'В работе'
    FINISHED = 'Завершена'

    STATUS_SET = ((CREATED, 'Создана'), (WORKS, 'Работает'), (FINISHED, 'Завершена'))

    name = models.CharField(max_length=150, verbose_name='Название рассылки')
    start_at = models.DateTimeField(default=datetime.now, verbose_name='Начало рассылки')
    stop_at = models.DateTimeField(default=datetime.now() + timedelta(days=1), verbose_name='Конец рассылки')
    next_send_time = models.DateTimeField(verbose_name='Время следующей отправки', **NULLABLE)
    periodicity = models.CharField(max_length=100, choices=PERIODICITY_SET, default=EVERY_DAY,
                                   verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=100, choices=STATUS_SET, default=CREATED, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение',
                                related_name='mailing_settings')
    client = models.ManyToManyField(Client, verbose_name='Клиент', related_name='mailing_settings')
    creator = models.ForeignKey(User, max_length=150, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Создатель')

    def __str__(self):
        return f'{self.name} Тема:{self.message.theme}. Периодичность:{self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['id']
        permissions = [
            ('Disabled_mailing', 'Disabled mailing'),
            ('view_all_list', 'view all list'),
        ]

    def save(self, *args, **kwargs):
        if not self.next_send_time:
            self.next_send_time = self.start_at
        super().save(*args, **kwargs)


class MailingLog(models.Model):
    SUCCESS = 'Успешно'
    ERROR = 'Ошибка'

    MAILING_STATUS_CHOICE = ((SUCCESS, 'Успешно'), (ERROR, 'Ошибка'))

    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Последняя попытка')
    status_attempt = models.CharField(choices=MAILING_STATUS_CHOICE, max_length=150, verbose_name='Статус попытки')
    response = models.TextField(**NULLABLE, verbose_name='Ответ почтового сервера')
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка',
                                related_name='mailing_log')
    creator = models.ForeignKey(User, max_length=150, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Создатель')

    def __str__(self):
        return f'Статус на {self.last_attempt} - {self.status_attempt}.'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'

import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail

from config import settings
from mailings.models import MailingSettings, MailingLog


def service_send_mails():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = MailingSettings.objects.filter(status__in=[MailingSettings.CREATED, MailingSettings.WORKS])

    for mailing in mailings:
        if current_datetime >= mailing.stop_at:
            mailing.status = mailing.FINISHED
            mailing.save()
            continue

        if mailing.next_send_time and current_datetime >= mailing.next_send_time:
            mailing.status = MailingSettings.WORKS
            mailing.save()

            try:
                response = send_mail(
                    subject=mailing.message.theme,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.client.all()],
                    fail_silently=False
                )

                MailingLog.objects.create(status_attempt=MailingLog.SUCCESS, response=response, mailing=mailing,
                                          creator=mailing.creator)
            except smtplib.SMTPException as error:
                MailingLog.objects.create(status_attempt=MailingLog.ERROR, response=str(error), mailing=mailing,
                                          creator=mailing.creator)

            if mailing.periodicity == MailingSettings.EVERY_DAY:
                mailing.next_send_time += timedelta(days=1)
            elif mailing.periodicity == MailingSettings.EVERY_WEEK:
                mailing.next_send_time += timedelta(weeks=1)
            elif mailing.periodicity == MailingSettings.EVERY_MONTH:
                mailing.next_send_time += timedelta(days=30)

            mailing.save()

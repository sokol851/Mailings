from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views.index import Index
from mailings.views.mailing import MailingSettingsListView, MailingSettingsUpdateView, MailingSettingsCreateView, \
    MailingSettingsDeleteView, MailingSettingsDetailView
from mailings.views.mailing_log import MailingLogListView
from mailings.views.message import MessageListView, MessageUpdateView, MessageCreateView, MessageDeleteView, \
    MessageDetailView
from mailings.views.client import ClientListView, ClientUpdateView, ClientCreateView, ClientDeleteView, ClientDetailView

app_name = MailingsConfig.name

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message_edit/<int:pk>", MessageUpdateView.as_view(), name="message_edit"),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message_delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),
    path("message_detail/<int:pk>", MessageDetailView.as_view(), name="message_detail"),

    path("client_list/", ClientListView.as_view(), name="client_list"),
    path("client_edit/<int:pk>", ClientUpdateView.as_view(), name="client_edit"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path("client_delete/<int:pk>", ClientDeleteView.as_view(), name="client_delete"),
    path("client_detail/<int:pk>", ClientDetailView.as_view(), name="client_detail"),

    path("mailing_list/", MailingSettingsListView.as_view(), name="mailing_list"),
    path("mailing_edit/<int:pk>", MailingSettingsUpdateView.as_view(), name="mailing_edit"),
    path("mailing_create/", MailingSettingsCreateView.as_view(), name="mailing_create"),
    path("mailing_delete/<int:pk>", MailingSettingsDeleteView.as_view(), name="mailing_delete"),
    path("mailing_detail/<int:pk>", MailingSettingsDetailView.as_view(), name="mailing_detail"),
    path('edit_status_mailing/<int:pk>/', MailingSettingsUpdateView.edit_status, name='edit_status_mailing'),

    path("log_list", MailingLogListView.as_view(), name="log_list"),

]

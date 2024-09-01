from django import forms
from django.forms import BooleanField

from mailings.models import Message, Client, MailingSettings


class StyleFormMixin:
    """ Миксин для изменения аттрибутов стилей. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    """ Форма для версий """

    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """ Форма для версий """

    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """ Форма для версий """

    class Meta:
        model = MailingSettings
        fields = '__all__'

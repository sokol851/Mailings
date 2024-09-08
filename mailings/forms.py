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
    """ Форма для сообщений """

    class Meta:
        model = Message
        exclude = ('creator', )


class ClientForm(StyleFormMixin, forms.ModelForm):
    """ Форма для клиентов """
    list_stop_word = ['Не указано', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    class Meta:
        model = Client
        exclude = ('creator', )

    def clean_first_name(self):
        """ Фильтрация запрещённых слов в названии """
        clean_data = self.cleaned_data['first_name']

        if clean_data is None:
            raise forms.ValidationError('Имя не может быть пустым или иметь цифры')
        else:
            for word in self.list_stop_word:
                if word.lower() in clean_data.lower():
                    raise forms.ValidationError('Имя не может быть пустым или иметь цифры')
        return clean_data

    def clean_last_name(self):
        """ Фильтрация запрещённых слов в названии """
        clean_data = self.cleaned_data['last_name']

        if clean_data is None:
            raise forms.ValidationError('Фамилия не может быть пустым или иметь цифры')
        else:
            for word in self.list_stop_word:
                if word.lower() in clean_data.lower():
                    raise forms.ValidationError('Фамилия не может быть пустым или иметь цифры')
        return clean_data


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """ Форма для рассылок """

    class Meta:
        model = MailingSettings
        # fields = '__all__'
        exclude = ('next_send_time', 'stop_at', 'creator', 'status', )

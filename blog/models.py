from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело статьи')
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', default='blog/none.jpg', verbose_name='Изображение',
                              **NULLABLE)
    count_views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)
    slug = models.CharField(max_length=100, verbose_name="slug", null=True, blank=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.title}'

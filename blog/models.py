from django.db import models
from django.urls import reverse_lazy

# Создание модели новости.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='media/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        'Category', 
        on_delete=models.PROTECT, null=True, verbose_name='Категория',
    )

    def get_absolute_url(self):
        return reverse_lazy('View_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

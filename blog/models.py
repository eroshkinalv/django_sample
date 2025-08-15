from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Текст')
    image = models.ImageField(upload_to='blog_images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    views_counter = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return f'{self.heading} - {self.created_at}'

    class Meta:
        verbose_name = 'запись в блоге'
        verbose_name_plural = 'запись в блоге'
        ordering = ['created_at']

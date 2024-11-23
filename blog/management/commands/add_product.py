from django.core.management.base import BaseCommand
from blog.models import Blog


class Command(BaseCommand):
    help = 'Добавьте новую запись в блог'

    def handle(self, *args, **kwargs):
        # Blog.objects.all().delete()

        blog, _ = Blog.objects.get_or_create(name='Блог 1', description='Запись 1', date='')

        blog_entry = [
            {'heading': 'Заголовок 1', 'content': 'Запись 1', 'image': 'image001.jpg'},
            {'heading': 'Заголовок 2', 'content': 'Запись 2', 'image': 'image001.jpg'},
            {'heading': 'Заголовок 3', 'content': 'Запись 3', 'image': 'image001.jpg'},
        ]

        for blog_data in blog_entry:
            blog, created = Blog.objects.get_or_create(**blog_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {blog.heading}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Blog already exists: {blog.heading}'))

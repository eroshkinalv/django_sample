from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog

from django.core.mail import send_mail


class BlogCreateView(CreateView):
    model = Blog
    fields = ('heading', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        if self.object.views_counter == 100:
            send_mail(
                "Поздравляем!",
                f"Поздравляем! У вашей записи '{self.object.heading}' 100 просмотров!",
                "eroshkina.liudmila.email@gmail.com",
                ["liudotchka@gmail.com"],
                fail_silently=False,
            )
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'content', 'image')
    success_url = reverse_lazy('blog:blog_detail')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

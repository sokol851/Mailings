from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.forms import BlogForm

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    form_class = BlogForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object.slug = slugify(self.object.title)
        return super().form_valid(form)

    @staticmethod
    def toggle_activity(request, pk):
        product_items = get_object_or_404(Blog, pk=pk)
        if product_items.is_published:
            product_items.is_published = False
        else:
            product_items.is_published = True
        product_items.save()
        return redirect(reverse('blog:blog_detail', args=(Blog.objects.get(id=pk).slug,)))


class BlogDeleteView(DeleteView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'
    success_url = reverse_lazy('blog:blog_list')

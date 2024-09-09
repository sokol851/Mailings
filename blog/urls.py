from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(3)(BlogListView.as_view()), name='blog_list'),
    path('<slug:the_slug_blog>/', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
    path('blog_create', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:the_slug_blog>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<slug:the_slug_blog>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity_blog/<int:pk>/', BlogUpdateView.toggle_activity, name='toggle_activity_blog'),
]

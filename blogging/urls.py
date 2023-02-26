from django.urls import path
from blogging.views import BlogListView
from blogging.views import detail_view

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]

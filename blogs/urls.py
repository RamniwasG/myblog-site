from django.urls import path
from . import views

urlpatterns = [
    path('', views.staring_page, name="starting-page"),
    path('posts', views.posts, name="all-posts-page"),
    path('posts/<slug:slug>', views.post_details, name="post-detail-page"),
]

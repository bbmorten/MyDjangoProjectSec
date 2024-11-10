from . import views
from django.urls import path

app_name="blog"

urlpatterns = [
    path('', views.FeaturedPostList.as_view(), name='home'),
    path('blog', views.allposts, name='blog_home'),
    path('blog/<slug:slug>/', views.category_post_list, name='post_category'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
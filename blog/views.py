# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Category, Post
from .forms import PostForm

class FeaturedPostList(generic.ListView):
    queryset = Post.objects.filter(status=1, featured=1).order_by('-created_on')
    template_name = 'home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def category_post_list (request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    context = {
        'category': category.title,
        'posts': posts,
    }
    return render(request, 'category.html', context)


def allposts(request):
    posts = Post.objects.order_by('-created_on')
    print(posts.count())
    context = {
        'posts': posts,
        }
    return render(request, 'blog.html', context)


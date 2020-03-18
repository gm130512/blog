from django.shortcuts import render
from .models import Post

# from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')


# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

# posts = [
#     {
#         'author': 'ABC',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 15, 2020'
#     },
# ]


def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    # 去哪 ，帶什麼過去
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

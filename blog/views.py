from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')


# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
posts = [
    {
        'author': 'ABC',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 15, 2020'
    },
    {
        'author': 'DFG',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 16, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # 去哪 ，帶什麼過去


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

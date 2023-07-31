from django.shortcuts import render
from .models import Blog


# Semua Blog
BLOGS = Blog.objects.all()

# List Berisi Kategori
CATS = []
for blog in BLOGS:
    if blog.category not in CATS:
        CATS.append(blog.category)


def index(request):
    context = {
        'HEADER': 'Blog Kang Joki :/',
        'SUBTITLE': 'Terbaru',
        'CATS': CATS,
        'BLOGS': BLOGS,
    }
    return render(request, 'blog/index.html', context)


def category(request, CAT_INPUT):
    context = {
        'HEADER': 'Blog Kang Joki :/',
        'SUBTITLE': f'Kategori : {CAT_INPUT}',
        'CATS': CATS,
        'BLOGS': Blog.objects.filter(category=CAT_INPUT),
    }
    return render(request, 'blog/index.html', context)


def blog(request, CAT_INPUT, SLUG_INPUT):

    # Databases
    BLOG = Blog.objects.get(slug=SLUG_INPUT)

    # Context
    context = {
        'HEADER': BLOG.title,
        'CATEGORY': CAT_INPUT,
        'AUTHOR': BLOG.author,
        'DATE': BLOG.date,
        'CONTENT': BLOG.content,
    }

    return render(request, 'blog/single_blog.html', context)

from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
from datetime import datetime as dt
from django.db.models import Q


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all(
    ).filter(
        Q(pub_date__lte=dt.now()),
        Q(is_published=True),
        Q(category__is_published=True)
    ).order_by('-pub_date')[0:5]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.now()),
        pk=id
    )

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = Post.objects.select_related(
        'category').filter(
            Q(pub_date__lte=dt.today()),
            Q(is_published=True),
            Q(category__is_published=True),
            Q(category__slug=category_slug)
    )

    category_list = get_object_or_404(Category.objects.all().filter(
        is_published=True,
        slug=category_slug,
        pub_date__lte=dt.today())
    )

    context = {
        'category': category_list,
        'post_list': post_list
    }
    return render(request, template, context)

from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
from django.db.models import Q
from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all(
    ).filter(
        Q(pub_date__lte=timezone.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    )[0:5]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    if Post.is_published and Category.is_published:
        post = get_object_or_404(Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()),
            pk=id
        )
        context = {'post': post}
        return render(request, template, context)
    else:
        raise 404


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = Post.objects.select_related(
        'category').filter(
            Q(pub_date__lte=timezone.now()),
            Q(is_published=True),
            Q(category__is_published=True),
            Q(category__slug=category_slug)
    )

    if Category.is_published:
        category_list = get_object_or_404(Category.objects.all().filter(
            is_published=True,
            slug=category_slug,
            pub_date__lte=timezone.now())
        )
    else:
        raise 404

    context = {
        'category': category_list,
        'post_list': post_list
    }
    return render(request, template, context)

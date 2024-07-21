from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post


DISP_LIMIT = 5


def index(request):
    context = {'post_list': Post.posts()[:DISP_LIMIT]}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, id):
    context = {'post': get_object_or_404(Post.posts(), pk=id)}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    post_list = Post.posts().filter(category__slug=category_slug)
    category = get_object_or_404(
        Category.objects.published(),
        slug=category_slug
    )

    context = {'category': category, 'post_list': post_list}
    template = 'blog/category.html'
    return render(request, template, context)

from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category

DISP_LIMIT = 5

posts = Post.published().filter(category__is_published=True)


def index(request):
    context = {'post_list': posts.check_time()[:DISP_LIMIT]}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(posts.check_time(), pk=id)
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    post_list = posts.check_time().filter(category__slug=category_slug)
    category = get_object_or_404(
        Category.published().check_time(),
        slug=category_slug
    )

    context = {'category': category, 'post_list': post_list}
    template = 'blog/category.html'
    return render(request, template, context)

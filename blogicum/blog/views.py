from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category

DISP_LIMIT = 5

POST_PB = Post.objects.filter(is_published=True)
CAT_PB = Category.objects.filter(is_published=True)

POST_CAT = Post.objects.select_related('category').filter(
    is_published=True,
    category__is_published=True
)


def time_check(self):
    return self.filter(pub_date__lte=timezone.now())


posts = time_check(POST_CAT)


def index(request):
    context = {'post_list': posts[:DISP_LIMIT]}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(posts, pk=id)
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    post_list = posts.filter(category__slug=category_slug)
    cat = get_object_or_404(time_check(CAT_PB), slug=category_slug)
    context = {'category': cat, 'post_list': post_list}
    template = 'blog/category.html'
    return render(request, template, context)

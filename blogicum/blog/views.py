from django.shortcuts import get_object_or_404, render

from django.utils import timezone

from blog.models import Post, Category


DISP_LIMIT = 5

POSTS = Post.objects.all()
POST_PB = POSTS.filter(is_published=True, pub_date__lte=timezone.now())
posts_cat = Post.objects.select_related('category').filter(
    is_published=True,
    category__is_published=True,
    pub_date__lte=timezone.now()
)

CATS = Category.objects.all()
CAT_PB = CATS.filter(is_published=True, pub_date__lte=timezone.now())


def index(request):
    template = 'blog/index.html'
    context = {'post_list': posts_cat[:DISP_LIMIT]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html',
    post = get_object_or_404(posts_cat, pk=id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    post_list = POST_PB.filter(category__slug=category_slug)
    category = get_object_or_404(CAT_PB.filter(slug=category_slug))

    context = {
        'category': category,
        'post_list': post_list
    }

    template = 'blog/category.html'

    return render(request, template, context)

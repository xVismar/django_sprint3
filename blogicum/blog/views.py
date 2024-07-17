from django.shortcuts import get_object_or_404, render
from blog.models import Post
from blog.models import Category
from django.db.models import Q
from django.utils import timezone


posts = Post.objects.select_related('category').filter(
    is_published=True,
    category__is_published=True,
    pub_date__lte=timezone.now()
)


def index(request):
    template = 'blog/index.html'
    context = {'post_list': posts[:5]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    if Post.is_published and Category.is_published:
        post = get_object_or_404(Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
            pk=id
        ))
        context = {'post': post}
        return render(request, template, context)
    else:
        raise 404


def category_posts(request, category_slug):
    template = 'blog/category.html'

    if Category.is_published:
        post_list = posts.filter(category__slug=category_slug)
        category_list = get_object_or_404(Category.objects.all().filter(
            Q(is_published=True)
            & Q(slug=category_slug))
        )
        context = {
            'category': category_list,
            'post_list': post_list
        }

        return render(request, template, context)

    else:
        raise 404

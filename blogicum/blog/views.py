"""Модуль обработки публикаций."""
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Q

from blog.models import Category, Post


def post_filter(queryset):
    return queryset.filter(is_published=True,
                           category__is_published=True,
                           pub_date__lte=timezone.now())


def index(request):
    posts = post_filter(Post.objects).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        post_filter(Post.objects.select_related('category')), Q(pk=id))
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = post_filter(category.posts)
    return render(request, 'blog/category.html', {
        'category': category, 'post_list': post_list})

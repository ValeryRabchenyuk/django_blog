from django.utils import timezone

from django.core.paginator import Paginator

from .constants import PAGINATOR_NUMBER

from django.db.models import Count

from django.shortcuts import get_object_or_404


def post_filter(queryset):
    return queryset.filter(is_published=True,
                           category__is_published=True,
                           pub_date__lte=timezone.now())


def post_paginator(request, queryset,
                   number_of_pages=PAGINATOR_NUMBER):
    paginator = Paginator(queryset, number_of_pages)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def count_comments(obj):
    """Подсчёт комментариев."""
    return obj.annotate(
        comment_count=Count('comments')
    ).all().order_by('-pub_date')


def get_object_or_404_with_author_check(model, id, request):
    """Проверка авторства."""
    obj = get_object_or_404(model, id=id)
    if request.user != obj.author:
        return None
    return obj

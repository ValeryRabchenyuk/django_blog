def post_filter(queryset):
    return queryset.filter(is_published=True,
                           category__is_published=True,
                           pub_date__lte=timezone.now())

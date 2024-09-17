from django.contrib import admin

from .models import Category, Location, Post, Comment

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'category',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = (
        'pub_date',
        'author',
        'location',
        'category',
        'is_published'
    )
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Comment)

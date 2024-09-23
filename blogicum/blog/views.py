"""Модуль обработки публикаций."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q,

from .forms import PostForm, CommentForm, UserForm
from .models import Category, Post, Comment, User
from .utils import post_filter, post_paginator, count_comments


def index(request):
    """Главная страница."""
    posts = count_comments(post_filter(Post.objects))
    page_obj = post_paginator(request, posts)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def post_detail(request, id):
    """Страница с информацией о посте."""
    posts = get_object_or_404(Post, Q(pk=id))
    if not posts.author == request.user:
        posts = get_object_or_404(post_filter(
            Post.objects.select_related('category', 'location', 'author')),
            id=id)
    form = CommentForm()
    comments = posts.comments.select_related('author')
    return render(request, 'blog/detail.html', {
        'post': posts, 'form': form, 'comments': comments})


def category_posts(request, category_slug):
    """Публикации в категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = post_filter(category.posts).order_by('-pub_date')
    page_obj = post_paginator(request, post_list)
    return render(request, 'blog/category.html', {
        'category': category, 'page_obj': page_obj})


def profile(request, username):
    """Страница пользователя."""
    profile = get_object_or_404(User, username=username)
    posts = count_comments(Post.objects.filter(author=profile))
    page_obj = post_paginator(request, posts)
    context = {'profile': profile,
               'page_obj': page_obj}
    return render(request, 'blog/profile.html', context)


@login_required
def edit_profile(request):
    """Редактирование страницы пользователя."""
    form = UserForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('blog:profile', username=request.user.username)
    context = {'form': form}
    return render(request, 'blog/user.html', context)


@login_required
def create_post(request):
    """Создание публикации."""
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect('blog:profile', request.user.username)
    context = {'form': form}
    return render(request, 'blog/create.html', context)


@login_required
def edit_post(request, id):
    """Редактирование публикации."""
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('blog:post_detail', id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', id)
    context = {'form': form}
    return render(request, 'blog/create.html', context)


@login_required
def delete_post(request, id):
    """Удаление публикации."""
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('blog:post_detail', id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    context = {'form': form}
    return render(request, 'blog/create.html', context)


@login_required
def add_comment(request, id):
    """Комментирование публикации."""
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('blog:post_detail', id)


@login_required
def edit_comment(request, id, comment_id):
    """Редактирование комментария."""
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('blog:post_detail', id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', id)
    return render(request, 'blog/create.html', {'form': form})


@login_required
def delete_comment(request, id, comment_id):
    """Удаление комментария."""
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('blog:post_detail', id)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', id)
    return render(request, 'blog/comment.html', {'comment': comment})

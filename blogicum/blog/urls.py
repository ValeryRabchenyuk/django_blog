from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
    # публикации
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
    # комментарии
    path('<int:id>/comment/', views.add_comment, name='add_comment'),
    path('<int:id>/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('<int:id>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    # профиль пользователя
    path('<slug:username>/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    ]

from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
    # публикации
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
    # комментарии
    path('posts/<int:id>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:id>/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('posts/<int:id>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    # профиль
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<slug:username>/', views.profile, name='profile'),
]

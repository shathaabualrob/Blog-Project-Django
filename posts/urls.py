from django.urls import path
from . import views
urlpatterns = [
    path('blog', views.index),
    # path('',  views.getPost,name='post'),
    path('<int:post_id>/post/', views.getPost, name='post'),
    path('categories/', views.getCategories, name='categories'),
    path('<int:category_id>/category/', views.getCategory, name='category'),
]
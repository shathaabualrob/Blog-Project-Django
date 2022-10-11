from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)
    # output = ','.join([p.title for p in posts])
    # blogcontents = ','.join([p.content for p in posts])
    # context = {'titles': output, 'bcontents': blogcontents }
    # return HttpResponse(output)
    # return HttpResponse("Hello World! You're at the polls index.")
    
def getPost(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {'post': post}
    return render(request, 'posts/post.html', context)

def getCategories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories/categories.html', context)

def getCategory(request, category_id):
    category = Category.objects.get(id = category_id)
    context = {'category': category}
    return render(request, 'categories/category.html', context)
from django.shortcuts import render
from .models import Post, Comment


# Create your views here.
def post_list(request):
    # return HttpResponse('hello')
    posts = Post.objects.all()
    # print(posts)
    return render(request, 'posts/post_list.html',{'posts': posts})

def comment_list(request):
    comment = Comment.objects.all()
    return render(request, 'posts/comment_list.html',{'comment': comment})

def post_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'posts/post_detail.html',{'post': post})
from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    # return HttpResponse('hello')
    posts = Post.objects.all()
    print(posts)
    return render(request, 'posts/post_list.html',{'posts': posts})
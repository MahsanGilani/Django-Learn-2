from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    # return HttpResponse('hello')
    return render(request, 'posts/post_list.html')
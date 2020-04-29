from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def all_blogs(request):
    #if you want all objects
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date') #If you want sorts the blogs as per date and returns the top 5 blogs then add  [:5] in the end
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

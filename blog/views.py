from django.shortcuts import render,get_object_or_404
from .models import HomePage,AboutPage,ContactPage,Post

def home (request):
    page=HomePage.objects.all()[0]
    posts=Post.objects.filter(status='PB')
    return render(request,'blog/home.html',{'page':page, 'posts':posts})

def about (request):
    page=AboutPage.objects.all()[0]
    return render(request,'blog/about.html',{'page':page})
def contact (request):
    page=ContactPage.objects.all()[0]
    return render(request,'blog/contact.html',{'page':page})
def post_detail(request,id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context = {
        'post': post,  # Add the 'post' object to the context
    }
    return render(request, 'blog/post_detail.html', context)
from django.shortcuts import render , redirect
from . models import *
from . forms import *

# Create your views here.


def index(request):
    # au = Author.objects.all()
    # aut = {'au' : au}
    blog = blogPost.objects.all()
    context = {'blog' : blog}
    return render(request , "app/index.html", context)

def blogPage(request , pk):
    blog = blogPost.objects.all()
    context = {'blog' : blog}
    return render(request , "app/blogPage.html" , context )

def addBlogs_page(request):
    
    # aut = {'au' : au}

    blogData = {'form' : addBlog()}
    return render(request , "app/addBlogs.html" , blogData)


def addBlogs(request):
 context = {}


 if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    pubDate = request.POST.get('pubData')
    author = request.POST.get('author')

 if title and content and pubDate and author:
    blog = addBlog( title = title , content = content ,pubDate = pubDate , author = author )
    blog.save()
    return redirect("/")

 else:
     context['msg'] = "Please provide all the details"
 blogData = {'form' : addBlog()}
 return render(request , "app/addBlogs.html" , blogData)

    
def authorData(request):
   blog = Author.objects.all()
   context = {'blog' : blog}

   return render(request , "app/authorData.html" , context)
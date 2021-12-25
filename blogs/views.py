from django.shortcuts import get_object_or_404, render
from .models import Post

def blog(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blog.html', context) 



def blogs(request):
 
   
    return render(request, 'blogs/blog.html',) 
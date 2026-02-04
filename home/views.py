from django.shortcuts import render
# Blog App se model import karein
from blog.models import BlogPost 

def home_index(request):
    # Sirf latest 3 posts nikalein ([:3] ka matlab first 3)
    latest_posts = BlogPost.objects.all().order_by('-pub_date')[:3]
    
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'home/index.html', context)
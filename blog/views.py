from django.shortcuts import render, get_object_or_404 # <-- Isko import jarur karein
from .models import BlogPost

def blog_index(request):
    all_posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'posts': all_posts})

# Naya Function
def blog_detail(request, pk):
    # Ye ID (pk) wala post dhoondhega, nahi mila to 404 Error dega
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})
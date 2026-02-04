from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    
    # <int:pk> ka matlab hai "Integer ID" (1, 2, 3...)
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
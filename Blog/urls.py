from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='HomePage'),
    path('createPost/', views.createPost, name='CreatePost'),
    path('editPost/<str:pk>/', views.editPost, name='EditPost'),
    path('deletePost/<str:pk>/', views.deletePost, name='DeletePost'),
    path('detailPost/<str:pk>/', views.detailPost, name='DetailPost'),
    path('about/', views.about, name='AboutPage'),
]
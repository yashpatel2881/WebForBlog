from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='LoginPage'),
    path('resetPassword/', views.resetPassword, name='ResetPassword'),
    path('register/', views.register, name='RegisterPage'),
    path('profile/', views.profile, name='ProfilePage'),
    path('editProfile/', views.editProfile, name='EditProfile'),
    path('logout/', views.logout, name='Logout')
]

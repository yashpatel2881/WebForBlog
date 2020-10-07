import os
from BlogApp import settings 
from django.core.mail import send_mail 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Profile, Profile
from Blog.models import Post

# Create your views here.

def register(request):

    if request.method == 'POST':
        
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, f"{username} Username is already Exist! Please, try different")

                return redirect('/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already Exist! Please try different")

                return redirect('/register')
            
            else:
                user = User.objects.create_user(
                    first_name = firstname,
                    last_name = lastname,
                    username = username,
                    email = email,
                    password = password1
                )

                user.save()
                
                profile_obj = Profile.objects.create(user=user)
                profile_obj.save()

                messages.success(request, f"You have Successfully Registered with {username}!")

                return redirect('/')

        else:
            messages.info(request, 'Password and Confirm Password are not match!')

            return redirect('/register')

    else:
        return render(request, 'users/register.html')

def login(request):

    auth.logout(request)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('/home')

        else:
            messages.info(request, 'Username or Password are Incorrect!')

            return redirect('/')        

    else:
        return render(request, 'users/login.html')

@login_required
def resetPassword(request):

    if request.method == 'POST':

        password1 = request.POST.get('newPassword1')
        password2 = request.POST.get('newPassword2')

        if password1 == password2:

            user = User.objects.get(id=request.user.id)
            user.set_password(password1)
            user.save()

            messages.info(request, 'Password reset successfully!')

            return redirect('/')

        else:
            messages.info(request, 'Password and Confirm Password are not match!')
            return redirect('/resetPassword')
        

    else:
        return render(request, 'users/resetPassword.html')

@login_required
def profile(request):

    postCount = Post.objects.filter(user_id=request.user.id).count()

    return render(request, 'users/profile.html', {'postCount': postCount})

@login_required
def editProfile(request):

    if request.method == 'POST' and request.FILES['image']:
        
        username = request.POST.get("username")
        email = request.POST.get("email")

        obj = User.objects.get(id=request.user.id)
        obj.username = username
        obj.email = email
        obj.save()

        image = request.FILES['image']

        print('image:',image)

        return redirect('/profile')
        
    else:
        return render(request, 'users/editProfile.html')

def logout(request):

    auth.logout(request)
    messages.info(request, 'You have been Logged out!')

    return redirect('/', messages)
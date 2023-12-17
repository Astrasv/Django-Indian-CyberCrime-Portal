from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save() # Saves the users in the admin page
            username = form.cleaned_data.get('username') # Validated data is in cleaned_data dictionary
            messages.success(request, 'Your account created has been created! You can login in')
            return redirect('blog-home') # blog-home is the NAME attr of the home page in blogApp
    else:
        form = UserRegisterForm()


    context = {
        'form':form
    }
        
    return render(request , 'users/register.html', context)

@login_required    
# This decorator allows to view the profile view only if the user is logged in. This is django inbuilt decorator

def profile(request):
    if request.method == 'POST':
        # instance = request.user used to populate the form with current user details
        # request.FILES is used to handle image files
        u_form = UserUpdateForm(request.POST, instance = request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')
            
            
        
        
    else:
        u_form = UserUpdateForm(instance = request.user) # instance = request.user used to populate the form with current user details
        p_form = ProfileUpdateForm(instance = request.user.profile)
        
    
    context = {
        'u_form': u_form,
        'p_form':p_form
    }
    
    return render (request,'users/profile.html',context)
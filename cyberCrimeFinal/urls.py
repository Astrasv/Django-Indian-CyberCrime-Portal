"""cyberCrimeFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'), # Instead of creating a urls inside users app, we are directly importing views here and adding users in project itself
    path('profile/', user_views.profile, name = 'profile'), 
        
    # Inbuild login page from auth. IN template_name we are asking to look for that directory for the HTML page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), 
    
    # Inbuild logout page from auth    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'), 
    
    path('', include('blogApp.urls')),
    path('records/' , include('MainTableInput.urls'))   
]


# Allows media to work in our browser

if settings.DEBUG == True:
    # Serve media files in development server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for band_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import the auth views
from band.views import UserLoginView, AdminLoginView, register  # Import custom login views

urlpatterns = [
    path('', include('band.urls')),  
    path('admin/', admin.site.urls),
    path('accounts/user/login/', UserLoginView.as_view(), name='user_login'),
    path('accounts/admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', register, name='registration'),  
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Password reset request form
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Password reset request submission success page
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Password reset form and token validation
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Password reset complete page
]
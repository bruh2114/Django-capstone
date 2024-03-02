from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import custom_login_view
from django.urls import reverse_lazy

app_name = 'band'
urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('songs/', views.songs, name='songs'),
    path('music/', views.music, name='music'),
    path('registration/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('band:home')), name='logout'),
]
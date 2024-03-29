from django.shortcuts import render, redirect
from .models import Member, Song, News, Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

def custom_login_view(request):
    """
    Custom login view for handling user authentication.
    
    Parameters:
    - request: HttpRequest object representing the incoming request
    
    Returns:
    - HttpResponse object for rendering the login page or redirecting to the home page
    """
    if request.user.is_authenticated:
        return redirect('band:home')  # Redirect to home if user is already authenticated
    else:
        return UserLoginView.as_view(template_name='band/login.html')(request)

def home(request):
    news = News.objects.order_by('-date')[:3]
    events = Event.objects.order_by('date')[:3]
    return render(request, 'band/home.html', {'news': news, 'events': events})

@login_required
def members(request):
    members = Member.objects.all()
    return render(request, 'band/members.html', {'members': members})

@login_required
def songs(request):
    songs = Song.objects.all()
    return render(request, 'band/songs.html', {'songs': songs})

@login_required
def music(request):
    # Add any logic you need for the music view
    return render(request, 'band/music.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('band:home')  # Redirect to the home page after successful registration
        else:
            # If the form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForm()
    return render(request, 'band/registration.html', {'form': form})

def registration_success(request):
    return render(request, 'band/registration_success.html')

class UserLoginView(BaseLoginView):
    """
    Custom user login view based on Django's BaseLoginView.
    
    Attributes:
    - template_name: The name of the template used for rendering the login page
    - success_url: The URL to redirect to after successful login
    """
    template_name = 'band/login.html'
    success_url = reverse_lazy('band:home')

class AdminLoginView(BaseLoginView):
    template_name = 'band/admin_login.html'
    success_url = reverse_lazy('admin:index')
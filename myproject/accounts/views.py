from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignupForm(request.POST) # email 까지 필드 확장한 Form(custom)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        # form = UserCreationForm()
        form = SignupForm() # email 까지 필드 확장한 Form(custom)
    return render(request, 'accounts/signup_form.html', {'form':form})


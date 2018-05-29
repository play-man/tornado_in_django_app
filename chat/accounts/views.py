from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *

# Create your views here.

def get_user_by_email(email):
	try:
		return User.objects.get(email=email)
	except User.DoesNotExist:
		return None

def login(request):

	from .forms import *
	if request.method == 'POST':
		#form = AuthenticationForm(request.POST)
		#if form.is_valid():
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email, password=password)
		auth_login(request, user)
		return redirect('profile')
	else:
		pass
	return render(request, "accounts/login.html")

def logout(request):
	auth_logout(request)
	return redirect('home')

def signup(request):
	
	from .forms import *
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			email = form.cleaned_data.get('email')
			password1 = form.cleaned_data.get('password1')
			user.set_password(password1)
			user.save()
			user = authenticate(email=email, password=password1)
			auth_login(request, user)
			return redirect('profile')
	else:
		pass
	return render(request, "accounts/signup.html")

def profile(request):
	if request.user.is_authenticated():
		user = User.objects.filter(username=request.user.username)
		return render(request, "accounts/profile.html", {'user': request.user})
	return HttpResponse('Unauthorized', status=401)
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import extenduser
from django.contrib.auth.models import User
from django.contrib import auth
from home import views

def signup(request):
	return render(request,'signup.html')

def login(request):
	return render (request,'login.html')

def sighupsubmit(request):
	if request.method == 'POST':
		if request.POST['pass1'] == request.POST['pass2']:
			try:
				user = User.objects.get(username =request.POST['uname'])
				return HttpResponse('Error Username Already exist')
			except User.DoesNotExist:
				user = User.objects.create_user(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],username = request.POST['uname'],password = request.POST['pass1'])
				phone = request.POST['number']
				DOB = request.POST['dob']
				new_extended_user = extenduser(mobile_no = phone , dateofbirth=DOB , user=user)
				auth.login(request,user)
				return redirect(views.afterlogin)
		else:
			return HttpResponse("Password Does Not Match")

	else:
		return render(request,'signup.html')

def loginsubmit(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['uname'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect(views.afterlogin)
		else:
			return render(request,'login.html',{'error':'Invalid Login Credentials'})

	else:
		return render (request,'login.html',{'error':'Worning'})

def logout(request):
	auth.logout(request)
	return redirect(views.index)

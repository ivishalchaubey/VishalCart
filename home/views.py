from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import items
from authuser import views
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


def index(request):
	our_items = items.objects

	return render(request,'index.html',{'itoms':our_items})

def detail(request,items_id):
	our_detail = get_object_or_404(items,pk=items_id)
	return render (request,'detail.html',{'full_detail':our_detail})

def afterlogin(request):
	our_items =items.objects
	return render (request,'afterlogin.html',{'itoms':our_items})

def upload(request):
 	return render(request,'upload.html')

def uploadetail(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('desc')
		price = request.POST.get('price')
		location = request.POST.get('location')
		email = request.POST.get('email')
		phone = request.POST.get('mobile')
		my_image = request.FILES['image']
		fs = FileSystemStorage()
		fs_name = fs.save(my_image.name,my_image)
		url = fs.url(fs_name)

		finalsave = items(name=name,description=description,price=price,location=location,email=email,phone=phone,photo=url)
		finalsave.save()
		# return redirect('/afterlogin/')
		return redirect(afterlogin)
	else:
		# return redirect('/afterlogin/')
		return redirect(uploadetail)



def profile(request):
	vishu = User.objects.all()	
	print(vishu)
	return render (request,'profile.html',{'user':vishu})


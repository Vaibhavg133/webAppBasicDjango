from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
	context={'posts':Post.objects.all()}
	return render(request,'blog/home.html',context)
	#return HttpResponse('<h1>Blog Home ABK</h1>')

def about(request):
	return render(request,'blog/about.html',{'title':'About'})
	#return HttpResponse('<h1>Blog About ABK</h1>')
# Create your views here.

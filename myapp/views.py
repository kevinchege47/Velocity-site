from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'home.html' , {})
def about(request):
	return render(request, 'about.html' , {})
def services(request):
	return render(request,'services.html',{})
def portfolio(request):
	return render(request,'portfolio.html',{})
def	team(request):
	return render(request,'team.html',{})
def contact(request):
	return render(request,'contact.html',{})



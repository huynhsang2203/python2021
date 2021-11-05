from django.shortcuts import render

# Create your views here.
def page_login(request):
    return render (request, './web/login.html')
def page_home(request):
    return render (request, './web/home.html')
    
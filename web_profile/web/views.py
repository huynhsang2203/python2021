from django.shortcuts import render, HttpResponse


# Create your views here.
def page_login(request):
    return render (request, './web/login.html')
def page_home(request):
    return render (request, './web/home.html')
def register(request):
    return render (request, './web/register_page.html')
def register_success(request):
    return render (request, './web/register_done.html')
from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.

def page_home(request):
    return render (request, './web/home.html')
def register(request):
    return render (request, './web/register_page.html')
def register_success(request):
    return render (request, './web/register_done.html')

class LoginClass(View):
    def get( self, request):
        return render (request, './web/login_page.html')
    def post( self, request):
        return render (request, './web/login_done.html')
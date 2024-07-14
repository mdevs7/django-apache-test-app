from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


class HomePage(View):
    def get(self,request):
        return render(request, 'index.html')


class RecurmentPage(View):
    def get(self,request):
        return render(request, 'recurments.html')


class ServicePage(View):
    def get(self,request):
        return render(request, 'services.html')


class SearchPage(View):
    def get(self,request):
        return render(request, 'search-jobs.html')
    
class CompanyPage(LoginRequiredMixin,View):
    def get(self,request):
        res = render(request, 'companies.html')
        res.set_cookie('name','client')
        res.set_cookie('theme','dark')
        return res


class LoginPage(View):
    def get(self,request):
        next_url = request.GET.get('next', '')
        context = {'next': next_url}
        print(context)
        return render(request, 'login.html',context)
    
    def post(self,request):
        next_url = request.POST.get('next','')
        print("NEXT URL: ", next_url)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        if user is None:
            return render(request, 'login.html')
        if authenticate(username=username, password=password):
            login(request,user=user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect(reverse_lazy("homepage"))
        else:
            return render(request, 'login.html')


class SignupPage(View):
    def get(self,request):
        return render(request, 'signup.html')
    
    def post(self,request):
        full_name = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).first() is not None:
            return render(request, 'signup.html')
        user = User.objects.create(username=username,last_name=full_name,email=email)
        user.set_password(password)
        user.save()
        print("User create successfully")
        return redirect('/login')


class LogoutPage(View):
    def get(self,request):
        logout(request)
        return redirect('homepage')

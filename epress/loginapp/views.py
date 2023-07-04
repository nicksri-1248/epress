from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.http import HttpResponseForbidden
from django.views import View
from django.views.generic import TemplateView

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'loginapp/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'loginapp/register.html', {'form': form})

class HomeView(LoginRequiredMixin,  View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class SuperView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'home.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        if not self.test_func():
            return HttpResponseForbidden()
        return render(request, self.template_name)

class LoginView(View):
    def get(self, request):
        return render(request, 'loginapp/login.html')

    def post(self, request):
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        user = authenticate(mobile_number=mobile_number, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'loginapp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'loginapp/login.html', {'error_message': 'Invalid login'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'loginapp/logout.html')

class IndexView(TemplateView):
    template_name = "main/home.html"

class ContactView(TemplateView):
    template_name = "main/contact.html"

class ServicesView(TemplateView):
    template_name = "main/services.html"

class AboutView(TemplateView):
    template_name = "main/about.html"

class HotelView(TemplateView):
    template_name = "main/hotel.html"

class RestaurantView(TemplateView):
    template_name = "main/restaurant.html"

class HospitalView(TemplateView):
    template_name = "main/hospital.html"

class SpaView(TemplateView):
    template_name = "main/spa.html"

class GymView(TemplateView):
    template_name = "main/gym.html"
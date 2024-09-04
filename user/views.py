from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.urls import reverse_lazy



# Create your views here.
def register(req):
    if(req.method == "POST"):
        register_form = forms.RegistrationForm(req.POST)
        if(register_form.is_valid):
            register_form.save()
            messages.success(req,'Signup Successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(req,'register.html',{'form':register_form,'type':'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self,form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.warning(self.request,'Invalid Login Credentials')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
def profile(req):
    return render(req,'profile.html')
    
def user_logout(req):
    logout(req)
    messages.warning(req,'You have been logged out of your account')
    return redirect('login')
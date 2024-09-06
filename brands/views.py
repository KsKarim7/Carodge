# from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

# Create your views here.

# @method_decorator(login_required,name = 'dispatch')
class AddBrandView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('add_brand')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
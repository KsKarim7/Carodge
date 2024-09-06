from django.shortcuts import render
from brands.models import Brand

def home(req):
    brands = Brand.objects.all()
    return render(req, 'home.html')
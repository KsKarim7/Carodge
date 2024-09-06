from django.shortcuts import render
from brands.models import Brand
from cars.models import Car

def home(req,brand_slug = None):
    cars = Car.objects.all()
    if(brand_slug is not None):
        brand = Brand.objects.get(slug = brand_slug)
        cars = cars.filter(brand = brand)
    brands = Brand.objects.all()
    return render(req, 'home.html', {'car' : cars, 'brand' : brands})
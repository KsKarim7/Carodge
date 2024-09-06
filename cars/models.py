from django.db import models
from brands.models import Brand
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField(default="0")
    price = models.IntegerField(default="0")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/media/uploads/', blank = True, null = True)
    def __str__(self):
        return self.name 
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('user/',include('user.urls')), 
    path('cars/',include('cars.urls')), 
    path('brand/',include('brands.urls')), 
    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_post'),
# 
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

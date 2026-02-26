from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to Online Medicine Shop") // "This is a placeholder view. You can replace it with an actual template later."

urlpatterns = [
    path('admin/', admin.site.urls),
  # path('', home, name='home'), NO need for this as we have medicines.urls handling the home page
    path('', include('medicines.urls')),
    path('', include('users.urls')),
    path('', include('cart.urls')),
    path('', include('orders.urls')),
]
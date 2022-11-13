from django.contrib import admin
from django.urls import path, include
from myapp.urls import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('myapp.urls')),
]

from django.contrib import admin
from django.urls import path, include
from thirdapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirectAtAuth),  
    path('http://127.0.0.1:8000/secondapp/login', login), 
    path('secondapp/', include('thirdapp.urls')),
]
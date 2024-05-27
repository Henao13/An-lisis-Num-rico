
from django.urls import path
from .views import analisis

urlpatterns = [
    path('', analisis, name='home'),     
    
    
    
]
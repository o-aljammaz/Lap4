from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name = "index"),
    path("taxrate",views.TRate,name = ""),
    path("<str:Amount>",views.taxCalculator,name = ""),
    
]
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("this is a site to calculate tax!")

def taxCalculator(request,Amount):
    Amount = int(Amount)
    finalAmount = (Amount * tax_rate) + Amount
    return HttpResponse(f"The total Amount after the tax: {finalAmount}")

def TRate(request):
    return HttpResponse(f"<h1> {tax_rate*100}% </h1>")
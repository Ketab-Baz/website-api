from django.http import HttpResponse
import datetime
from django.shortcuts import render

def sign_in(request):
    return render(request, 'sign-in.html')

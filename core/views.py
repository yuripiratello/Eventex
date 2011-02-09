# Create your views here.
from django.shortcuts import render_to_response

def homepage(request):
    return render_to_response('index.html')

def homepage2(request):
    return render_to_response('index2.html')

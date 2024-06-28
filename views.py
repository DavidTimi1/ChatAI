from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from dotenv import dotenv_values

# Create your views here.
def index(request):
    return render(request, "chatAI/index.html")


def askAI(request):
    if request.method == 'post':
        if not request.POST.get('prompt'):
            return Http404()
        prompt = request.POST["prompt"]




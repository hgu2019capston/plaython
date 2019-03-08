from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Applicant
from .forms import PostForm

import random, string

def createForm(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            applicant = form.save()
            applicant.password = makeRandomString()
            applicant.generate()
            
            return result(request, applicant.password)

    else:
            form = PostForm()

    return render(request, 'playton/form.html', {'form':form})


def makeRandomString():
    randomStream = ""
    for i in range(0,10):
        randomStream += str(random.choice(string.ascii_letters))
    return randomStream


def result(request, user_pwd):
    return HttpResponse("Saved Successfully! <br> This is your future password. You have to keep this with screen capture or something. <br>" + user_pwd)

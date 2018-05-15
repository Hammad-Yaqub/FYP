from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from PlayNLearn.forms import signUpForm
from django.forms import forms


def home_view(request):
    return render(request,"login/index.html")

def signUp_add(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.email = request.email
            signup.uname = request.uname
            signup.password = request.password
            signup.date_created = timezone.now()
            signup.save()
            return render(request, "login/index.html")
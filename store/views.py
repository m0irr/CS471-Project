from django.shortcuts import render

def home(request):
    nmbOfPhase = {'Phase':'One'}
    return render(request,'home.html',nmbOfPhase)

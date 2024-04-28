from django.shortcuts import render
from .forms import LoginForms
def home(request):
    nbPhase = {'Phase':3}
    return render(request,'store/home.html',nbPhase)

def about(request):
    nb_phase = {'Phase':'three'}
    return render(request,'store/about.html',nb_phase)

def login(request):
    if request.method=='POST':
        data=LoginForms(request.POST)
        if data.is_valid:
            data.save()
    return render(request,'store/login.html',{'lf':LoginForms})
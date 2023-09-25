from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def register(request):
    return render(request,'register.html',{})

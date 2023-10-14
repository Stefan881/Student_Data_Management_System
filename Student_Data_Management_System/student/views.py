from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,SignInForm
from .models import Student
from django.http import HttpResponse





# Create your views here.
def header(request):
     context = {}
     return render(request,'header.html',context)

def homepage(request):
     context = {}
     return render(request,'homepage.html',context)


def home(request):
    # Check to see if loging in 
    records = Student.objects.all()
    if request.method == 'POST':
      
        form = SignInForm(request.POST)
        username  = request.POST['username']
        password = request.POST['password']
        # Authenticate

        user = authenticate(request,username=username,password=password)
        if user is not None:
            username  = request.POST['username']
            login(request,user)
            messages.success(request,f'Welcome {username}')
            return render(request,'home.html',{'form':form,'records':records,'username':username})
            #return redirect(home)
            
        else:
            username  = request.POST['username']
            messages.success(request,"Something went wrong please try again...")
            return redirect('home')
    else:
           form = SignInForm()
           return render(request,'home.html',{'form':form,'records':records})
        


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f"You have succefully registered.Welcome{username}!")
            return redirect('home')
        
    else:
            form = SignUpForm()
            return render(request,'register.html',{'form':form})
        

      
def logout_student(request):
    logout(request)
    messages.success(request,"You have been logged out....")
    return redirect('home')





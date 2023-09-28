from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,SignInForm



# Create your views here.
def home(request):
    # Check to see if loging in 

    if request.method == 'POST':
        #form = SignInForm(request.POST)
        username  = request.POST['username']
        password = request.POST['password']

        # Authenticate

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in successfully...")
            return redirect('home')
        else:
            messages.success(request,"Something went worng please try again...")
            return redirect('home')
    else:
        form = SignInForm()
        return render(request,'home.html',{'form':form})
        


def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	
    


def logout_student(request):
    logout(request)
    messages.success(request,"You have been logged out....")
    return redirect('home')





from django.shortcuts import render,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib import messages




# Create your views here.


############################ index page ####################
def home(request):
    if request.user.is_authenticated: 
        return render(request,'index.html')
    else:                               
        return HttpResponseRedirect('/register/')
    

############################ Register page ###################
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.add_message(request,messages.SUCCESS,"successfully created!!!")
            form.save()
            return HttpResponseRedirect('/')
            
        return render(request,'registration/register.html',{'form':form})

    form = RegistrationForm()
    return render(request,'registration/register.html',{'form':form})

from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pm = fm.cleaned_data['password']
        reg = User(name=nm, email=em, password=pm)
        reg.save()
        fm = StudentRegistration()
    else:
     fm = StudentRegistration() 
    stud = User.objects.all() 
    return render(request, 'addandshow.html', {'form':fm,'stu':stud})


    #This Function will delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#This function will update or edit
def update_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi= User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi) 
    return render(request, 'updatestu.html',{'form':fm})

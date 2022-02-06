from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Reg
from .models import Book
# Create your views here.

def add_show(request):
    if request.method =='POST':
        fm=Reg(request.POST)
        if fm.is_valid():
            
            a=fm.cleaned_data['name']
            b =fm.cleaned_data['img']
            c=fm.cleaned_data['summary']
            obj=Book(name=a,img=b,summary=c)
            obj.save()
            fm=Reg()
            return HttpResponseRedirect(request.path)
    else:
        fm=Reg()
    
    b= Book.objects.all()
    return render(request,'books/addandshow.html', {'form':fm, 'bb':b})

def update_data(request,id):
    if request.method =='POST':
        pi=Book.objects.get(pk=id)
        fm=Reg(request.POST,instance=pi)
        if fm.is_valid:
            fm.save()
    else:
         #if method is get
         pi=Book.objects.get(pk=id)
         fm=Reg(instance=pi)
    
    return render(request,'books/update.html', {'form':fm})

def delete_data(request, id):
    if request.method=='POST':
        pi=Book.objects.get(pk=id) #pk primary key
        pi.delete()
    return HttpResponseRedirect('/')



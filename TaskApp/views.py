from django.shortcuts import render,redirect
from . import forms
from . import models
def Tesk(request):
    if request.method=="POST":
        form=forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Teskapp")
    else:    
        form=forms.TaskForm()
    return render(request,'task.html',{'form':form})

def edit_tesk(request,id):
    fm=models.TaskModel.objects.get(pk=id)
    form=forms.TaskForm(instance=fm)
    if request.method=="POST":
        form=forms.TaskForm(request.POST,instance=fm)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    
    return render(request,'task.html',{'form':form})

def delete_tesk(request,id):
     fm=models.TaskModel.objects.get(pk=id)
     fm.delete()
     return redirect ('homepage')
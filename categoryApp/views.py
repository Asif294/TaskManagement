from django.shortcuts import render,redirect
from . import forms
def Category(request):
    if request.method=="POST":
        form=forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Categoryapp')
    else:
        form=forms.CategoryForm()
    return render(request,'category.html',{'form':form})

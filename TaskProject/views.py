from django.shortcuts import render,redirect
from TaskApp.models import TaskModel
def home(request):
    deta=TaskModel.objects.all()
    return render(request,'home.html',{'deta':deta})
from django.shortcuts import render,redirect
from .models import input_model,getTodo
from django.http.response import HttpResponseRedirect
# Create your views here.
def home_view(request):
    submitted=False
    if request.method=="POST":
        getText=getTodo(request.POST)
        if getText.is_valid():
            getText.save()
            return HttpResponseRedirect('/')

    else:
         getText=getTodo
         if 'submitted' in request.GET:
             submitted=True
    

    showTodo=input_model.objects.all()
    
    return render(request,'index.html',{'getText':getText,'showTodo':showTodo})


def delete_todo(request,todo_id):
    deleteList=input_model.objects.get(pk=todo_id)
    deleteList.delete()
    return redirect('/')
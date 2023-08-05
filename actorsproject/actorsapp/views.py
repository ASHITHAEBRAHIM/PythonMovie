from django.shortcuts import render, redirect
from .models import actors
from .form import actorsform
# Create your views here.
def index(request):
    Actors = actors.objects.all()
    return render(request,"index.html",{'Actors_list':Actors})
def detail(request,id):
    Actors = actors.objects.get(id=id)
    return render(request,"detail.html",{'Actors_list':Actors})
def add(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Age = request.POST['Age']
        Desc = request.POST['Desc']
        Image = request.FILES['Image']
        Actors = actors(Name=Name,Age=Age,Desc=Desc,Image=Image)
        Actors.save()
    return render(request,"add.html")
def update(request,id):
    Actors = actors.objects.get(id=id)
    forms = actorsform(request.POST or None,request.FILES,instance =Actors)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,"update.html",{'form':forms,'actors':Actors})
def delete(request,id):
    if request.method =='POST':
        Actors = actors.objects.get(id=id)
        Actors.delete()
        return redirect('/')
    return render(request,"delete.html")
from django.http import HttpResponse
from django.shortcuts import render

from . models import place

from . models import team

# Create your views here.
# def demo(request):
    # return HttpResponse("hello world")

def demo(request):
    obj=place.objects.all()
    obbj=team.objects.all()
    return render(request,"index.html",{'result':obj, 'answ':obbj})

#def about(request):
    #return render(request,"about.html")

#def fund(request):
  # name="india"
   # return render(request,"home.html",{'obj':name})

#def addition(request):
   # x=int(request.GET["num1"])
   # y=int(request.GET["num2"])
   # res=x+y
   # return render(request,"result.html",{"result":res})
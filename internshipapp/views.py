from django.shortcuts import render,redirect
from internshipapp.models import Product, User, Login, Post
from django.http import HttpResponse
import time, datetime

def home(request):
    return render(request,"home.html")

def user(request):
    return render(request,"user.html")

def adduser(request):
    if request.method == 'POST':
        data = User()
        data.username="na"
        data.first_name=request.POST.get('name1')
        data.last_name=request.POST.get('name2')
        data.email=request.POST.get('mail')
        data.password=request.POST.get('password')
        data.save()
        data.username="USERNAME"+str(data.id)
        data.save()
        data1=Login()
        data1.Username=data.username
        data1.Password=data.password
        data1.Category="user"
        data1.save()
        return render(request,"user.html")

def product(request):
    if 'uid' not in request.session:
                return render(request,'login.html')
    else:
        return render(request,"product.html")

def addproduct(request):
    if request.method == 'POST':
        data = Product()
        data.name=request.POST.get('name')
        data.weight=request.POST.get('weight')
        data.price=request.POST.get('price')
        data.created_at=datetime.datetime.now().strftime('%H:%M:%S')
        data.updated_at=request.POST.get('utime')
        data.save()
        return render(request,"product.html")

def login(request):
    return render(request,"login.html")

def log(request):
    if request.method == 'POST':
        dataa=Login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        
        flag=0
            
        for da in dataa:
            if un == da.Username and pwd == da.Password:
                type=da.Category
                request.session['uid']=un
                flag = 1
                if type=="admin":
                    return redirect('/home')
                          
                elif type=="user":
                    return redirect('/post')      
                
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")

def post(request):
    if 'uid' not in request.session:
                return render(request,'login.html')
    else:
        ui=request.session['uid']
        data=User.objects.get(username=ui)
        return render(request,"post.html",{'uid':data})

def addpost(request):
    if request.method == 'POST':
        data = Post()
        data.user=request.POST.get('name1')
        data.text=request.POST.get('name2')
        data.created_at=datetime.datetime.now().strftime('%H:%M:%S')
        data.updated_at=request.POST.get('utime')
        data.save()
        return render(request,"post.html")

def logout(request):
    del request.session['uid']
    return redirect('/home')


# Create your views here.

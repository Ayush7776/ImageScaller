from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def sighup(request):
    return render(request,"app/Sighnup.html")
def login(request):
    return render(request,"app/Login.html")
def index(request):
        try:
            imagekey=request.session['id']
            images=UploadedImage.objects.filter(imagekey=imagekey)
        except:
            return render(request,"app/Index.html")
            
        imagekey=request.session['id']
        images=UploadedImage.objects.filter(imagekey=imagekey)
        return render(request,"app/Index.html",{'key':images})
def validatesighup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        user=Student.objects.filter(Email=email)
        if user:
            msg="User Allready Exiests..!"
            return render(request,"app/Sighnup.html",{'msg':msg})
            
        if password==cpassword:
            newuser=Student.objects.create(FirstName=fname,LastName=lname,Email=email,Phone=phone,Password=password)
            msg="Your Account Has Been Created Please Login With Credentials"
            return render(request,"app/Login.html",{'msg':msg})
        else:
            msg="PassWord Or Confirm PassWord Does Not Match..!"
            return render(request,"app/Sighnup.html",{'msg':msg})

def validatelogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=Student.objects.get(Email=email)
        if user:
            request.session['id']=user.id
            request.session['firstname']=user.FirstName
            request.session['lastname']=user.LastName
            request.session['email']=user.Email
            return redirect('index')
        else:
            msg="Please Login Using Correct Credetials"
            return redirect('sighup')

def logout(request):
    del request.session['id']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    return redirect('login')

def uploadpage(request):
    return render(request,"app/upload.html")

def uploadimg(request):
    if request.method=="POST":
        id=request.session['id']
        can=Student.objects.get(id=id)
        image=request.FILES['image']
        imagekey=request.session['id']
        insert=UploadedImage.objects.create(imagekey=can,image=image)
        return redirect('index')

def AdminLoginPage(request):
    return render(request,"app/admin.html")

def AdminLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        if username=="admin" and password=="123":
            user=Student.objects.all()
            return render(request,"app/adminCotrolls.html",{'user':user})
        else:
            msg="Please Login Using Correct Credetials"
            return render(request,"app/admin.html",{'msg':msg})
            
def EditPage(request,pk):
    getdata=Student.objects.get(id=pk)
    getimages=UploadedImage.objects.filter(imagekey=pk)
    return render(request,"app/Edit.html",{'key2':getdata,'images':getimages})

def UpdateData(request,pk):
    udata=Student.objects.get(id=pk)
    udata.FirstName=request.POST['fname']
    udata.LastName=request.POST['lname']
    udata.Email=request.POST['email']
    udata.Phone=request.POST['contact']
    udata.save()
    return redirect('AdminLoginPage')

def DeleteData(request,pk):
    deletedata=Student.objects.get(id=pk)
    deletedata.delete()
    return redirect('AdminLoginPage')

def DeleteImg(request,pk):
    deletedata=UploadedImage.objects.get(id=pk)
    deletedata.delete()
    return redirect('AdminLoginPage')
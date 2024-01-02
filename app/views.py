from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer


def sighup(request):
    return render(request,"app/Sighnup.html")
def login(request):
    return render(request,"app/Login.html")
def videos(request):
    return render(request,"app/videos.html")
def about(request):
    return render(request,"app/about.html")
def contact(request):
    return render(request,"app/contact.html")
def index(request):
        try:
            imagekey=request.session['id']
            images=UploadedImage.objects.filter(imagekey=imagekey)
        except:
            return render(request,"app/Index.html")
            
        imagekey=request.session['id']
        images=UploadedImage.objects.filter(imagekey=imagekey)
        return render(request,"app/Index.html",{'key':images})


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        msg="Your Account Has Been Created Please Login With Credentials"
        return render(request,"app/Login.html",{'msg':msg})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=Student.objects.get(Email=email,Password=password)
        except:
            msg="Please Login Using Correct Credetials"
            return render(request,"app/Login.html",{'msg':msg})
        
        user=Student.objects.get(Email=email,Password=password)
        if user:
            request.session['id']=user.id
            request.session['firstname']=user.FirstName
            request.session['lastname']=user.LastName
            request.session['email']=user.Email
            return redirect('index')
           

def logout(request):
    del request.session['id']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    return render(request,"app/Login.html")

def uploadpage(request):
    return render(request,"app/upload.html")

def uploadimg(request):
    if request.method=="POST":
        id=request.session['id']
        can=Student.objects.get(id=id)
        image=request.FILES['image']
        caption=request.POST['caption']
        imagekey=request.session['id']
        insert=UploadedImage.objects.create(imagekey=can,image=image,caption=caption)
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
    udata.Password=request.POST['password']
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
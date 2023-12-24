from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
   path('',views.index,name="index"),
   path('validatesighup',views.validatesighup,name="validatesighup"),
   path('login',views.login,name="login"),
   path('validatelogin',views.validatelogin,name="validatelogin"),
   path('sighup',views.sighup,name="sighup"),
   path('logout',views.logout,name="logout"),
   path('uploadpage',views.uploadpage,name="uploadpage"),
   path('uploadimg',views.uploadimg,name="uploadimg"),

]




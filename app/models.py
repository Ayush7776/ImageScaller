from django.db import models

class Student(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone=models.BigIntegerField()
    Password=models.CharField(max_length=50,default="")


class UploadedImage(models.Model):
    imagekey=models.ForeignKey(Student,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
